import PySimpleGUI as sg

sg.theme('darkamber')

SYMBOLS = """ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-=`!@#$%^&*()_+~,./?;"':[{]}\\|"""
key = 17
SYMBOLS_length = len(SYMBOLS)
chiper_text = ''


layout = [
    [sg.Text("Caeser Chiper", auto_size_text=True)],
    [sg.HSeparator()],
    [
    sg.Text(text="Message", auto_size_text=True),
    sg.In(size=(20, 20), justification="center", font="monospace", enable_events=True, key="message"),
    ],
    [
        sg.Radio(text="Encrypt", group_id="mode", enable_events=True, key="encrypt", default=True),
        sg.Radio(text="Decrypt", group_id="mode", enable_events=True, key="decrypt", default=False)
    ],
    [sg.Text(text='chiper text', enable_events=True, auto_size_text=True, justification='center', key='translated')],
    [sg.Text(text="copy text", auto_size_text=True, justification="center", enable_events=True, key="copy")],
    [sg.HSeparator()],
    [sg.Button(button_text='Exit')]
]

window = sg.Window('caeser\'s chiper', layout=layout, finalize=True, element_justification="center")

while True:
    event, values = window.read(timeout=10)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == "message":
        message = values['message']
        window['copy'].update('copy text')
        translated_text = ''
        for char in message:
            if char in SYMBOLS:
                char_index = SYMBOLS.find(char)
                if values['encrypt']:
                    translated_index = char_index + key
                elif values['decrypt']:
                    translated_index = char_index - key
                if translated_index >= SYMBOLS_length:
                    translated_index -= SYMBOLS_length
                elif translated_index < 0:
                    translated_index += SYMBOLS_length
                translated_text = translated_text + SYMBOLS[translated_index]
            else:
                translated_text = translated_text + char
        chiper_text = translated_text
        window['translated'].update(chiper_text)
    
    if event == 'copy':
        sg.clipboard_set(chiper_text)
        window['copy'].update("copied")

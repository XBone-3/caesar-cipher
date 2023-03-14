import sys

SYMBOLS = """ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-=`!@#$%^&*()_+~,./?;"':[{]}\\|"""

message = sys.argv[1]

key = 8

mode = sys.argv[2]

translated_message = ''

for char in message:
    if char in SYMBOLS:
        symbols_char_index = SYMBOLS.find(char)
        if mode.lower() == 'e':
            encrypted_char_index = symbols_char_index + key
        elif mode.lower() == 'd':
            encrypted_char_index = symbols_char_index - key
        if encrypted_char_index >= len(SYMBOLS):
            encrypted_char_index = encrypted_char_index - len(SYMBOLS)
        if encrypted_char_index < 0:
            encrypted_char_index = encrypted_char_index + len(SYMBOLS)
        translated_message = translated_message + SYMBOLS[encrypted_char_index]
    else:
        translated_message = translated_message + char

print(translated_message)
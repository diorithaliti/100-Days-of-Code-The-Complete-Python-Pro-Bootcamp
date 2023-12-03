#TEXT TO MORSE ENCRYPTER

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', ' ':'/',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def dh_text_to_morse(text):
    converted = ''
    for each_letter in text:
        converted += MORSE_CODE_DICT[each_letter.upper()] + ' '
    return converted

def dh_morse_to_text(text):
    splited_text = text.split(" ")
    converted = ''
    for each_letter in splited_text:
        for keys, value in MORSE_CODE_DICT.items():
            if each_letter == value:
                converted += keys
    return converted


choose = input("Enter text you want to convert to morse or text: \n")

encrypted_text = dh_text_to_morse(choose)
if choose[0] == "." or choose[0] =="-":
    decrypted_text = dh_morse_to_text(choose)
    print(f"Text: {decrypted_text}")
else:
    print(f"Morse Code: {encrypted_text}")






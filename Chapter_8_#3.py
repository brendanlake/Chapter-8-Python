def encrypt():
    global sentence
    sentence = input('Enter a sentence: ')
    for i in sentence:
        char = codes.get(i, '')
        print(char, end='')
    print('')
def decrypt():
    print(sentence)
    

codes = {
    'A': '@',
    'a': '9',
    'B': '%',
    'b': '#',
    'C': '^',
    'c': '&',
    'D': '3',
    'd': '1',
    'E': '!',
    'e': '$',
    'F': '2',
    'f': '(',
    'G': ')',
    'g': '8',
    'H': '7',
    'h': '&',
    'I': '0',
    'i': '6',
    'J': '5',
    'j': '`',
    'K': '~',
    'k': ':',
    'L': '{',
    'l': '}',
    'M': '<',
    'm': '>',
    'N': '|',
    'n': '=',
    'O': '+',
    'o': '-',
    'P': '_',
    'p': '4',
    'Q': '?',
    'q': '/',
    'R': ',',
    'r': '.',
    'S': '[',
    's': ']',
    'T': '\'',
    't': '\\',
    'U': ';',
    'u': 's',
    'V': 'w',
    'v': 'j',
    'W': 't',
    'w': 'p',
    'X': 'q',
    'x': 'c',
    'Y': 'z',
    'y': 'u',
    'Z': 'f',
    'z': 'k',
    ' ': ' ',
    '.': '.'
}
encrypt()
decrypt()


    

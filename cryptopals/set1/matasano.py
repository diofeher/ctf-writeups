import base64
import string

FREQUENCY = {'A': 8.17, 'C': 2.78, 'B': 1.29, 'E': 12.7, 'D': 4.25, 'G': 2.02, 'F': 2.23, 'I': 6.97, 'H': 6.09, 'K': 0.77, 'J': 0.15, 'M': 2.41, 'L': 4.03, 'O': 7.51, 'N': 6.75, 'Q': 0.1, 'P': 1.93, 'S': 6.33, 'R': 5.99, 'U': 2.76, 'T': 9.06, 'W': 2.36, 'V': 0.98, 'Y': 1.97, 'X': 0.15, 'Z': 0.07, 'a': 8.17, 'c': 2.78, 'b': 1.29, 'e': 12.7, 'd': 4.25, 'g': 2.02, 'f': 2.23, 'i': 6.97, 'h': 6.09, 'k': 0.77, 'j': 0.15, 'm': 2.41, 'l': 4.03, 'o': 7.51, 'n': 6.75, 'q': 0.1, 'p': 1.93, 's': 6.33, 'r': 5.99, 'u': 2.76, 't': 9.06, 'w': 2.36, 'v': 0.98, 'y': 1.97, 'x': 0.15, 'z': 0.07}

def hex_to_b64(text):
    hx = text.decode('hex')
    return base64.b64encode(hx)


def xor_strings(text1, text2):
    lst = [chr(ord(a) ^ ord(b)) for a, b in zip(text1, text2)]
    return ''.join(lst)


def score(text):
    score = 0
    for i in text:
        if i in string.letters + ' ':
            score += 1
    return score
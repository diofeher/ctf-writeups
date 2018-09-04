import base64
import string
import binascii
from itertools import izip_longest

FREQUENCIES = {
    'a': 0.0651738, 'A': 0.0651738,
    'b': 0.0124248, 'B': 0.0124248,
    'c': 0.0217339, 'C': 0.0217339,
    'd': 0.0349835, 'D': 0.0349835,
    'e': 0.1041442, 'E': 0.1041442,
    'f': 0.0197881, 'F': 0.0197881,
    'g': 0.0158610, 'G': 0.0158610,
    'h': 0.0492888, 'H': 0.0492888,
    'i': 0.0558094, 'I': 0.0558094,
    'j': 0.0009033, 'J': 0.0009033,
    'k': 0.0050529, 'K': 0.0050529,
    'l': 0.0331490, 'L': 0.0331490,
    'm': 0.0202124, 'M': 0.0202124,
    'n': 0.0564513, 'N': 0.0564513,
    'o': 0.0596302, 'O': 0.0596302,
    'p': 0.0137645, 'P': 0.0137645,
    'q': 0.0008606, 'Q': 0.0008606,
    'r': 0.0497563, 'R': 0.0497563,
    's': 0.0515760, 'S': 0.0515760,
    't': 0.0729357, 'T': 0.0729357,
    'u': 0.0225134, 'U': 0.0225134,
    'v': 0.0082903, 'V': 0.0082903,
    'w': 0.0171272, 'W': 0.0171272,
    'x': 0.0013692, 'X': 0.0013692,
    'y': 0.0145984, 'Y': 0.0145984,
    'z': 0.0007836, 'Z': 0.0007836,
    ' ': 0.1918182
}

def hex_to_b64(text):
    hx = text.decode('hex')
    return base64.b64encode(hx)


def xor_strings(text1, text2):
    lst = [chr(ord(a) ^ ord(b)) for a, b in zip(text1, text2)]
    return ''.join(lst)


def naive_score(text):
    score = len(text)
    for i in text:
        if i in string.letters + ' ':
            score -= 1
    return score


def score(text):
    printable = ''.join([c for c in text if c in string.printable])
    non_printable = ''.join([c for c in text if c not in string.printable])
    bs = printable + non_printable
    expected = {}
    for char, value in FREQUENCIES.items():
        expected[ord(char)] = value * len(bs)
    observed = {}

    many_non_letter_characters = 0
    for c in text:
        if not c in string.printable:
            return float('inf')
        elif c in (string.digits + string.punctuation):
            many_non_letter_characters += 1
        else:
            observed[c] = observed.get(c, 0) + 1

    score = 0
    for k in expected:
        score += abs(expected[k] - observed.get(k, 0))
    score += abs(many_non_letter_characters - .085 * len(bs))
    return score


def break_single_xor(line, score=score):
    best_text = ''
    best_score = float('inf')
    for i in range(256):
        res = xor_strings(line.strip().decode('hex'), chr(i)*len(line))
        points = score(res)
        if points < best_score:
            best_text = res
            best_score = points
    return best_text, best_score


def ascii_to_bin(text):
    if text == '':
        return
    return bin(int(binascii.hexlify(text),16))[2:]


def hamming_distance(t1, t2):
    score = 0
    for c1, c2 in zip(ascii_to_bin(t1), ascii_to_bin(t2)):
        if c1 != c2:
            score += 1
    return score


def encrypt_repeated_xor(text, key):
    output = ''
    for i, c in enumerate(text):
        indice = i % len(key)
        output += chr(ord(c) ^ ord(key[indice]))
    return output


def calculate_keysize(ciphertext):
    # Return top 5 probably keysizes
    lst = []
    TOTAL_CHUNKS = 20
    for keysize in range(3, 40):
        chunks = []
        total = keysize * TOTAL_CHUNKS
        if total > len(ciphertext):
            total = len(ciphertext)
        for i in range(0, keysize * TOTAL_CHUNKS, keysize):
            chunks.append(ciphertext[i:keysize + i])
        distances = []
        from itertools import combinations
        for p in combinations(range(len(chunks)), r=2):
            distances.append(hamming_distance(chunks[p[0]], chunks[p[1]]) / float(keysize))
        average_distance = sum(distances) / len(distances)
        lst.append((average_distance, keysize))
    lst.sort(key=lambda p: p[0])
    return lst[:5]


def break_repeated_xor(ciphertext):
    keysizes = calculate_keysize(ciphertext)
    best_key = ''
    best_key_score = 0
    for _, keysize in keysizes:
        key = ''
        blocks = [ciphertext[i:i+keysize] for i in range(0, len(ciphertext), keysize)]
        transposed_blocks = [''.join(block) for block in izip_longest(*blocks, fillvalue='')]

        for block in transposed_blocks:
            best_text = ''
            best_score = float('inf')
            best_char = ''
            for i in range(32, 128):
                res = xor_strings(block, chr(i)*len(block))
                points = score(res)
                if points < best_score:
                    best_text = res
                    best_score = points
                    best_char = chr(i)
            key += best_char
            naive_points = naive_score(key)
        if naive_points > best_key_score:
            best_key = key
            best_key_score = naive_points
    return best_key

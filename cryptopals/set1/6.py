import binascii
import base64
from matasano import score, xor_strings, hamming_distance, encrypt_repeated_xor, naive_score, break_repeated_xor

a1 = 'this is a test'
a2 = 'wokka wokka!!!'

assert hamming_distance(a1, a2) == 37

def main():
    with open('6.txt', 'r') as f:
        ciphertext = base64.b64decode(f.read().strip())

    best_key = break_repeated_xor(ciphertext)
    print encrypt_repeated_xor(ciphertext, best_key)
    print 'KEY FOUND: ', best_key
    assert best_key == 'Terminator X: Bring the noise'

main()

import operator
import string
from matasano import xor_strings, naive_score, break_single_xor

ciphertext = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
results = {}

text = break_single_xor(ciphertext, score=naive_score)
assert text[0] == "Cooking MC's like a pound of bacon"

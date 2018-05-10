import operator
import string
from matasano import xor_strings, score

text = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
results = {}

for i in range(256):
    res = xor_strings(text.decode('hex'), chr(i)*len(text))
    results[chr(i)] = {'score': score(res), 'text': res} 

top_3_items = sorted(results.items(), key=lambda obj: (obj[1]['score']), reverse=True, )[:3]
assert top_3_items[0][1]['text'] == "Cooking MC's like a pound of bacon"
from matasano import score, xor_strings

best_score = 0
best_text = ''

with open('4.txt') as f:
    for line in f.readlines():
        for i in range(256):
            res = xor_strings(line.strip().decode('hex'), chr(i)*len(line))
            points = score(res)
            if points > best_score:
                best_text = res
                best_score = points

print best_score, best_text
assert best_text.strip() == 'Now that the party is jumping'
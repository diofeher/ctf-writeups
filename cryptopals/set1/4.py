from matasano import score, xor_strings, break_single_xor, naive_score

best_score = float('inf')
best_text = ''

with open('4.txt') as f:
    for line in f.readlines():
        res, score = break_single_xor(line, score=naive_score)
        if score < best_score:
            best_text = res.strip()
            best_score = score

print best_text, best_score
assert best_text == 'Now that the party is jumping'

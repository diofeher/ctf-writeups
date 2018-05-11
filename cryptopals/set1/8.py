import base64

BLOCK_SIZE = 16

with open('8.txt') as f:
    text = f.readlines()

for line in text:
    line = line.strip()
    chunks = []
    for i in range(0, len(line), BLOCK_SIZE):
        chunks.append(line[i:i+BLOCK_SIZE])
    if len(chunks) != len(set(chunks)):
        print chunks
        break

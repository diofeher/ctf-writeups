result=1
for i in range(1, 100):
    result *= i

print sum([int(char) for char in str(result)])
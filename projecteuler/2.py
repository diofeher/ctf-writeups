# dumb 
LIMIT = 4000000

a, b = 0, 1
sum = 0
while b<LIMIT:
    a, b = b, a+b
    if not b % 2:
        sum += b
    
print sum

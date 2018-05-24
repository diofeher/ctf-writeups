def all_perms(string):
    if len(string) <=1:
        yield string
    else:
        for perm in all_perms(string[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + string[0:1] + perm[i:]

def is_prime(num):
    if num==0 or num==1: return False
    if num==2: return True
    for i in range(2, num/2):
        if not num%i:
            return False
    return True
    
def is_circular_prime(num):
    perms = list(all_perms(str(num)))
    all_primes = [number for number in perms if is_prime(int(number))]
    return len(all_primes) == len(perms)
        
print len([i for i in range(1000000) if is_circular_prime(i)])
def fibonacciDynamic(n):
    fib = [0] * (n + 2)
    fib[1] = 1
    if n <= 1:
        return fib
    for i in range(2, n + 1):
        res = fib[i - 1] + fib[i - 2]
        fib[i] = res
        if res > n:
            break
    return fib[:i+1]

# [0, 1, 1, 2, 3, 5, 8, 13]
def solution(A):
    if not A:
        return 1
    N = len(A)
    fib = fibonacciDynamic(N)
    # print 'fib list', fib, 'N:', N
    pos = -1
    last_pos = -1
    jumps_count = 0
    banks = [i for i, val in enumerate(A) if val]
    banks.append(len(A))
    # print 'banks', banks
    while pos < N:
        for i in reversed(fib):
            if i + pos in banks:
                last_pos = pos
                pos += i
                jumps_count += 1
                # print 'i', i, 'i+pos', i + pos, 'banks', banks, 'i + pos in banks', i + pos in banks, 'jumps', jumps_count
                break
        if pos == last_pos:
            return -1

    return jumps_count 

assert solution([0,0,0,1,1,0,1,0,0,0,0]) == 3
assert solution([]) == 1
assert solution([1]) == 1

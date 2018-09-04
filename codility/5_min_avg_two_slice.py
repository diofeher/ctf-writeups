from __future__ import division

def prefix_sums(A):
    n = len(A)
    P = [0] * (n+1)
    for k in range(1, n+1):
        P[k] = P[k-1] + A[k-1]
    return P

def solution(A):
    # write your code in Python 3.6
    min_value = 99000
    indice = None
    length = len(A)
    prefs = prefix_sums(A)
    for i in range(len(A)-1):
        count = 1
        while count <= 2:
            if i+1+count > length:
                count += 1
                continue
            value = (prefs[i+1+count] - prefs[i]) / (i+1+count-i)
            # print 'value', prefs[i+count] - prefs[i], 'i', i, 'count', count, A[i:i+count]
            if value < min_value:
                min_value = value
                indice = i
            count += 1
    # print indice
    return indice

assert solution([10000, -10000]) == 0
assert solution([4, 2, 2, 5, 1, 5, 8]) == 1
assert solution([-3, -5, -8, -4, -10]) == 2
from functools import reduce # Valid in Python 2.6+, required in Python 3
import operator
from itertools import combinations

def solution(A):
    length = len(A)
    if length <= 3:
        reduce(operator.mul, A, 1)
    max_value = -9999999999999999999999999
    if length >= 6:
        A.sort()
        elements = A[:3] + A[-3:]
    else:
        elements = A
    for items in combinations(elements, 3):
        value = reduce(operator.mul, items, 1)
        if value > max_value:
            max_value = value
    return max_value

assert solution([-5, 5, -5, 4]) == 125
assert solution([4, 5, 1, 0]) == 20
assert solution([-10, -2, -4]) == -80
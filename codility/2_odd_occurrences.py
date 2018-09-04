from collections import Counter

def solution(A):
    # write your code in Python 3.6
    for key, value in Counter(A).items():
        if value % 2 == 1:
            return key

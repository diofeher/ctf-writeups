def solution(A):
    length = len(A)
    if length < 3:
        return 0
    A.sort()
    for i in range(len(A)-2):
        if A[i] + A[i+1] > A[i+2]:
            return 1
    return 0


assert solution([10, 2, 5, 1, 8, 20]) == 1
assert solution([10, 50, 5, 1]) == 0
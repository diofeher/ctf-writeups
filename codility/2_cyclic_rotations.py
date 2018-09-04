def solution(A, K):
    length = len(A)
    answer = [0] * length
    for i, val in enumerate(A):
        pos = i+K
        if pos >= length:
            pos = pos % length
        answer[pos] = val
    return answer


assert solution([1,2,3,4 ], 4) == [1,2,3,4]
assert solution([1], 4) == [1]
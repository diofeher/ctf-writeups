def solution(A):
    missing = 1
    for i in range(max(A) + 2):
        if i > 0:
            if i not in A:
                missing = i
                break
    return missing

assert solution([1,3,6,4,1,2]) == 5
assert solution([1,2,3]) == 4
assert solution([-1, -3]) == 1
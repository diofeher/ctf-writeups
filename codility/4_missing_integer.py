def solution(A):
    missing = 1
    for elem in sorted(A):
        if elem == missing:
            missing += 1
        if elem > missing:
            break
    return missing

assert solution([1,3,6,4,1,2]) == 5
assert solution([1,2,3]) == 4
assert solution([-1, -3]) == 1
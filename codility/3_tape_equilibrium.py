def solution(A):
    head = A[0]
    tail = sum(A[1:])
    min_dif = abs(head - tail)
    for index in range(1, len(A)-1):
        head += A[index]
        tail -= A[index]
        if abs(head-tail) < min_dif:
            min_dif = abs(head-tail)
    return min_dif


assert solution([3,1,2, 4 ,3])==1
assert solution([3,10]) == 7
assert solution([-1000, 1000]) == 2000
assert solution([1, 1]) == 0
assert solution([-10, -20, -30, -40, 100]) == 20
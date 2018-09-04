def solution(A):
    if sum(set(A)) == sum( range(1, len(A)+1) ):
        return 1
    return 0

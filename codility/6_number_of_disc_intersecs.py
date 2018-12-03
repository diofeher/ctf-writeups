# def solution(A):
#     length = len(A)
#     left = []
#     right = []
#     for i, elem in enumerate(A):
#         left.append( i - elem )
#         right.append( i + elem )
#     left.sort()
#     right.sort()
#     print left, right
#     return 11
def solution(A):
    B = [0] * len(A) * 2
    print B
    for i, elem in enumerate(A):
#         left.append( i - elem )
#         right.append( i + elem )

assert solution([1, 5, 2, 1, 4, 0]) == 11
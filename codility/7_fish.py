def solution(A, B):
    '''
    Assuming:
        upstream = 0
        downstream = 1
    '''
    stack = []
    remaining = 0
    for fish, position in zip(A, B):
        if position == 0:
            if not stack:
                remaining += 1
            else:
                while stack and fish > stack[-1]:
                    stack.pop()
                if not stack:
                    remaining += 1
        else:
            stack.append(fish)
    return remaining + len(stack)

assert solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]) == 2
assert solution([0, 1], [1, 1]) == 2
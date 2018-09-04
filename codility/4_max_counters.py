# NEED TO REWORK ON THAT
def solution(N, A):
    # write your code in Python 3.6
    RESP = [0] * N
    MAX_OPERATION = N + 1
    current_max = 0
    current_min = 0
    for operation in A:
        print operation, MAX_OPERATION
        if operation != MAX_OPERATION:
            if RESP[operation-1] <= current_min:
                RESP[operation-1] = current_min + 1
            else:
                RESP[operation-1] += 1

            if RESP[operation-1] > current_max:
                current_max = RESP[operation-1]
        else:
            # MAXING!
            if current_min == current_max:
                current_min += 1
            else:
                current_min = current_max
    
    for i, val in enumerate(RESP):
        if val < current_min:
            RESP[i] = current_min
    print RESP
    return RESP


# assert solution(5, [3, 4, 4, 6, 1, 4, 4]) == [3, 2, 2, 4, 2]
assert solution(1, [2, 1, 1, 2, 1]) == [3]
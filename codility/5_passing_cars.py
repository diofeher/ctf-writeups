def prefix_sums(A):
    n = len(A)
    P = [0] * (n+1)
    for k in range(1, n+1):
        if A[k-1] == 1:
            P[k] = P[k-1] + A[k-1]
        else:
            P[k] = P[k-1]
    return P


def solution(A):
    # write your code in Python 3.6
    pref = prefix_sums(A)
    total = 0
    for i, val in enumerate(A):
        if val == 0:
            total += pref[-1] - pref[i]
    if total > 1000000000:
        return -1
    return total
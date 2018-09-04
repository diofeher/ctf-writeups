
def solution(S, P, Q):
    values = dict(A=1, C=2, G=3, T=4)
    length = len(S)
    A = [-1] * length
    C = [-1] * length
    G = [-1] * length
    T = [-1] * length
    mappings = dict(A=A, C=C, G=G, T=T)

    for i, char in enumerate(S):
        mappings[char][i] = values[char]

    return R

assert solution('CAGCCTA', [2, 5, 0], [4, 5, 6]) == [2,4,1]
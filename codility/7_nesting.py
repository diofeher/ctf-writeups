def solution(S):
    count = 0
    for char in S:
        if char == "(":
            count += 1
        else:
            if count == 0:
                return 0
            count -= 1
    if count == 0:
        return 1
    else:
        return 0

assert solution("(()(())())") == 1
assert solution("())") == 0
assert solution(")(") == 0
def digit_sum(n):
    s = 0
    while n:
        s, n = s + n % 10, n / 10
    return s

def fatorial_sum(inp):
    number = int(inp)
    summ = 0
    for i in xrange(number+1):
        if i>=10:
            summ += digit_sum(i)
        else:
            summ += i
    print summ


# digit_sum(1234)
fatorial_sum("BMC_TEST_INPUT_MAGIC")
# fatorial_sum("0")
# fatorial_sum("1")
# fatorial_sum("10")
# fatorial_sum("100")
# fatorial_sum("1000")
# fatorial_sum("1000000")
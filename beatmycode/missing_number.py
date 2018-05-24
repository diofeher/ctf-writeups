def missing_number(inpt):
    N, seq = inpt.split(':')
    lst = seq.split(',')
    for i in xrange(1, int(N)+1):
        if str(i) not in lst:
            print i
            break


missing_number("BMC_TEST_INPUT_MAGIC")
# missing_number("8:1,2,3,4,5,6,8")
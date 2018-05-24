import sys

def color(inp):
    N, M = inp.split(',')
    for row in xrange(int(M)):
        for column in xrange(int(N)):
            value = 0 if (row+column) % 2 == 0 else 1
            sys.stdout.write(str(value))
        sys.stdout.write('\n')
    sys.stdout.flush()

color("BMC_TEST_INPUT_MAGIC")
# color("7,4")
# color("10,2")
# color("2,10")
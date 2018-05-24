# solution one
print sum([i for i in xrange(1000) if not i%5 or not i%3])

# solution two
print sum(set(range(0, 1000, 3))|set(range(0, 1000, 5)))
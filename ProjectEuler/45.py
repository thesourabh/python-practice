import sets

t = [i * (i + 1) / 2 for i in xrange(100000)]
p = [i * (3 * i - 1) / 2 for i in xrange(100000)]
h = [i * (2 * i - 1) for i in xrange(100000)]

print set(t).intersection(p).intersection(h)
def fact(n):
	if (n < 2):
		return 1
	else:
		return fact(n - 1) * n

"""
nCr = n!/( r! * (n-r)! )

"""
count = 0
for n in xrange(1, 101):
	for r in xrange(1, n + 1):
		ncr = fact(n) / (fact(r) * fact(n-r))
		if (ncr > 1000000):
			count += 1
print count
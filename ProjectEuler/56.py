maximum = 0
for a in xrange(100):
	for b in xrange(100):
		p = a ** b
		psum = 0
		while (p > 0):
			psum += p % 10
			p /= 10
		if (psum > maximum):
			maximum = psum
print maximum
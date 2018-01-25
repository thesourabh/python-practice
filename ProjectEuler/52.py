
def getSet(n):
	s = set()
	while(n > 0):
		s.add(n % 10)
		n /= 10
	return s


for i in xrange(125875,1258750):
	s = set()
	n = getSet(i)
	j = 2
	while (j <= 6):
		m = getSet(i * j)
		if (m == n):
			j += 1
		else:
			break
	if (j > 6):
		print i
def rev(n):
	r = 0
	while(n > 0):
		r = r * 10 + (n % 10)
		n /= 10
	return r

count = 0
for i in xrange(1, 10000):
	j = 0
	n = i
	while (j < 50):
		r = rev(n)
		n = n + r
		if rev(n) == n:
			break
		j += 1
	if (j >= 50):
		count += 1
print count
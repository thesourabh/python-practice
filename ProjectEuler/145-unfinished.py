def rev(n):
	r = 0
	if (n % 10 == 0):
		return 2000000000
	while(n > 0):
		r = r * 10 + (n % 10)
		n /= 10
	return r

def reversible(n):
	while (n > 0):
		if (n % 10 % 2 == 0):
			return False
		n /= 10
	return True

count = 0
for i in xrange(1, 500000):
	n = i + rev(i)
	if (reversible(n)):
		count += 1
print count
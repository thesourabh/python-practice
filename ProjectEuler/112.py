def ascend(n):
	d = n % 10
	n /= 10
	while(n > 0):
		if (d < n % 10):
			return False
		d = n % 10
		n /= 10
	return True

def descend(n):
	d = n % 10
	n /= 10
	while(n > 0):
		if (d > n % 10):
			return False
		d = n % 10
		n /= 10
	return True

count = 0
n = 1
while (count * 100 / n != 99.0):
	if (not ascend(n) and not descend(n)):
		count += 1
	n += 1

print "N:", n
print "Count:", count
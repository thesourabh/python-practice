def is_bin_palin(n):
	b=""
	while(n>0):
		b=b + str(n%2)
		n/=2
	return (b==b[::-1])

def is_palin(n):
	return (str(n)==(str(n)[::-1]))

sum=0
for i in xrange(10000):
	if(is_palin(i) & is_bin_palin(i)):
		sum+=i
print sum
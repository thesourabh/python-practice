def is_prime(n):
	flag=0
	for i in xrange(2,n/2 + 1):
		if(n%i==0):
			return 0
	return 1

count=0
lim=1000000
num=[0 for i in range(lim)]
for i in xrange(2,lim):
	if(num[i]==0):
		j=2
		while(i*j<lim):
			num[i*j]=1
			j+=1
c=0
j=0
flag=0
for i in xrange(len(num)):
	if(num[i]==0):
		flag=0
		c=i
		j=0
		while(c>0):
			c/=10
			j+=1
		l=j
		n=i
		for j in range(l):
			n= ( ( 10**(l-1) ) * ( n%10 ) ) + n/10
			if ( num[n]==1 ):
				flag=1
				break
		if(flag==0):
			count+=1

print count-2
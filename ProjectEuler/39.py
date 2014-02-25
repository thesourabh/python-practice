max=0
count=0
for n in xrange(120,1000):
	count=0
	for i in xrange(1,n/3):
		for j in xrange(i,n/2):
			c=n-(i+j)
			if(c<1):
				continue
			if( i*i + j*j == c*c):
				count+=1
	if (count>max):
		max=count
print max
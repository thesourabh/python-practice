sum=2
flag=0
i=3
while(i<2000000):
	j=2
	flag=0
	while(j<=int(i**.5)):
		if(i%j==0):
			flag=1
		j=j+1
	if(flag==0):
		print i
		sum=sum+i
	i=i+1
print sum
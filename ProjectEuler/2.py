sum=0
a=0
b=1
while(b<=4000000):
	print a
	print b
	if(a%2==0):
		sum=sum+a
	if(b%2==0):
		sum=sum+b
	a=a+b
	b=b+a
print sum
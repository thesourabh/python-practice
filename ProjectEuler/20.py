n=100
prod=1
for i in range(1,n+1):
	prod=prod*i
copy=prod
sum=0
while(copy>0):
	digit=copy%10
	sum=sum+digit
	copy/=10
print sum
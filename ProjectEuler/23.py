def sum(n):
	sum=0
	for i in range(1,n/2 + 1):
		if( n%i==0 ):
			sum+=i
	return (sum>n)

count=0
abn=[]
num=[z for z in range(28124)]
tot=0
for i in range(28124):
	tot+=i
	if(i%1000==0):
		print i
	if(sum(i)):
		abn.append(i)
print "\n\n\n",len(abn),"\n\n\n"
for i in range(len(abn)):
	for j in range(len(abn)):
		x=abn[i]+abn[j]
		if(x<28124):
			tot-=num[x]
			num[x]=0
print tot
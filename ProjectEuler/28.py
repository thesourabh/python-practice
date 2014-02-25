sum=1
tot=1
for i in range(2,1001,2):
	tot+=sum+i
	tot+=sum+i*2
	tot+=sum+i*3
	tot+=sum+i*4
	sum=sum+i*4

print tot

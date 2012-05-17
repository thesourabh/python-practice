
def collatz(n):
	count=0
	n+=n
	while(n>1):
		if(n%2==0):
			n=n/2
		else:
			n=3*n+1
		count+=1
	print "\n\n\n"
	return count

max=0
num=0
for i in range(1000000,0,-1):
	if(i%10000):
		print "\n\n",i,"\n\n"
	chlen=collatz(i)
	if(chlen>=max):
		max=chlen
		num=i
print "\n\n\n\n\n",max,num


#837799
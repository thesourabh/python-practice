
def s(n):
    sum=0
    for i in range(1,n):
	if(n%i==0):
	    sum+=i
    return sum

n=0
sum=0
while(n<10000):
    a=s(n)
    b=s(a)
    if((b==n) & (b!=a)):
	sum+=n
    n+=1
print sum

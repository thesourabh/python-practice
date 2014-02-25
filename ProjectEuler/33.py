from decimal import Decimal

print Decimal(3/20)
num=1
den=1

for i in range(10,100):
	if(i%10==0):
		continue
	for j in range(i+1,100):
		if(j%10==0):
			continue
		a=str(i)
		b=str(j)
		if( ( (float(a[0])/float(b[0])==float(i)/float(j)) & (a[1]==b[1]) ) | ( (float(a[0])/float(b[1])==float(i)/float(j)) & (a[1]==b[0]) ) | ( (float(a[1])/float(b[0])==float(i)/float(j)) & (a[0]==b[1]) ) | ( (float(a[1])/float(b[1])==float(i)/float(j)) & (a[0]==b[0]) ) ):
			print i,j,"   ",
			num*=i
			den*=j

for i in range(2,100):
	while( (num%i==0) & (den%i==0) ):
		num/=i
		den/=i

print "\n\nAnswer: ",den
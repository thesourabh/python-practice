fil=open('13.txt')
cents=[int(x) for x in fil]
sum=0
for i in cents:
	sum+=i
while (sum>=int(1e+10)):
	sum/=10
print sum
fil.close()
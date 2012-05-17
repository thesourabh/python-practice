a=[2]
flag=0
i=3
while(len(a)<10001):
	j=2
	flag=0
	while(j<=int(i**.5)):
		if(i%j==0):
			flag=1
		j=j+1
	if(flag==0):
		a.append(i)
	i=i+1
print len(a),a[len(a)-1]
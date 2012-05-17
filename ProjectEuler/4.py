la=0
for i in range(100, 1000):
	for j in range(100, 1000):
		pro=i*j
		copy=pro
		rev=0
		while(copy>0):
			rev=rev*10+copy%10
			copy=copy/10
		if((pro==rev)&(pro>la)):
			la=pro
print la		
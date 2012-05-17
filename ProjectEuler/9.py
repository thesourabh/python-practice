a=1
b=2
for i in range(1,500):
	for j in range(1,i):
		k=i*i + j*j
		k=k**.5
		if((i+j+k)==1000):
			print int(j*i*k)
def triang(n):
	t=0
	for i in range(1,n+1):
		t=t+i
	return t

def divisors(tri):
	fact=1
	for j in range(1,(tri/2)+1):
		if(tri%j==0):
			fact+=1
	return fact



fact=0
i=10000
max=2
maxi=2
while(i<14000):
	if(i%100==0):
		print i,
	tri=triang(i)
	fact=divisors(tri)
	if(fact>max):
		max=fact
		maxi=i
	i+=1
print max,maxi,triang(maxi)


#<5000
#320 2079 2162160
#320 4640 10767120
#320 5264 13857480

#<10000
#480 5984 17907120

#<14000
#576 12375 76576500
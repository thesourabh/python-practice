n = 600851475143
div = [x for x in range(2,int(n**.5)) if n % x == 0]
i, j = 0, len(div) - 1
while j >=0:
	print div[j]
	j=j-1
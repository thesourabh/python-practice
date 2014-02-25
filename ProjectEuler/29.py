
s=[]

for i in range(2,101):
	for j in range(2,101):
		s.append(i**j)
s=set(s)
print len(s)

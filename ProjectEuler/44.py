import sets
p1 = [i * (3 * i - 1) / 2 for i in xrange(1,10000)]
p = set(p1)
for i in p:
 for j in p:
  if (i + j) in p:
   if abs(i - j) in p:
    print i,j,"   Answer: ",j-i



#1560090 7042750
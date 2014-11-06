import decimal
n = 100
line = 0
for i in xrange(1,n+1):
 if line == 0:
  print
  sp = round((abs(n/2 - i)/2.5) - 0.2)
  while sp > 0:
   print " ",
   sp-=1
  s = abs(n/2 - i)
  line = abs((n/2 - s)/2)
 else: line -= 1
 if ( i / 10 ) == 0:
  print i," ",
 else:
  print str(i)+" ",
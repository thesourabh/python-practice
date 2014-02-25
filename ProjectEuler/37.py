def is_prime(n):
 if n < 2:
  return False
 for i in xrange(2,n/2 + 1):
  if(n % i == 0):
   return False
 return True

 

#count = 0
#sum = 0
count = 1
sum = 739397 #Got the eleventh number after checking numbers above 700,000
for i in xrange(10,10000):
 if( (i % 10 != 2) & (i % 10 != 3) & (i % 10 != 5) & (i % 10 != 7)):
  continue
 c = i
 dig = 0
 while(c > 0):
  if not is_prime(c):
   break
  dig += 1
  c = c / 10
 if c == 0:
  c = i
  while(c>0):
   if not is_prime(c):
    break
   c = c % (10**(dig-1))
   dig -= 1
  if c == 0:
   print i
   count += 1
   #if count > 11:
   if count > 11:
    break
   sum += i

print "Sum:",sum,"\nCount:",count
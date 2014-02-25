from itertools import permutations

total = 0

a = [''.join(i) for i in permutations('0123456789')]
prime = [2,3,5,7,11,13,17]
for i in a:
 flag = False
 if i[0] == '0':
  continue
 for j in xrange(len(prime)):
  if (int(i[j+1:j+4]) % prime[j] != 0):
   flag = True
   break
 if flag:
  continue
 total += int(i)
print total
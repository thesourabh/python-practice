import time

start = time.clock()
max = num = 0
for i in xrange(10000):
 if (str(i)[0] != '9'):
  continue
 dig = []
 flag = 0
 n = 1
 while (flag == 0):
  ans = str(i * n)
  n += 1
  for j in ans:
   if (j in dig) or (j == '0'):
    flag = 1
    break
   dig.append(j)
   if (len(dig) > 9):
    flag = 1
    break
  if ((flag == 0) and (len(dig) == 9)):
   flag = 2
   break
 if flag == 2:
  cur = int(''.join(dig))
  if cur > max:
   max = cur
   num = i
end = time.clock()    

print 'Pandigital: ', max, ' Number: ', num
print end-start, ' seconds'
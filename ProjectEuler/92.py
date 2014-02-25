def calc(num):
 s = 0
 while num > 0:
  d = num % 10
  s += d ** 2
  num /= 10
 if s == 1:
  return False
 elif s == 89:
  return True
 else:
  return calc(s)

count = 0
for i in xrange(1,10000000):
 if calc(i): count += 1

print count
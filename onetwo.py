

def numDig(n,x):
 if n == 0:
  return
 st = str(x)
 ans = ""
 while st != "":
  a = st[0]
  cnt = 0
  i = 0
  while i < len(st) and a == st[i]:
   cnt += 1
   i += 1
  st = st[i:]
  ans = ans+str(cnt)+a
 print x
 numDig(n-1,int(ans))

n = int(raw_input("\nHow many numbers of the series to print? "))
print "\nSeries:"
numDig(n,1)
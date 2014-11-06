F = open("A-large-practice.in")
O = open("A-large-practice.out","w")

N = int(F.readline())
for i in xrange(N):
 C = int(F.readline())
 I = int(F.readline())
 P = F.readline().split(' ')
 for item_1 in xrange(I - 1):
  for item_2 in xrange(item_1 + 1, I):
   a = int(P[item_1])
   b = int(P[item_2])
   if a + b == C:
    O.write("Case #"+str(i+1)+": "+str(item_1+1)+" "+str(item_2+1)+"\n")

O.close()
F.close()
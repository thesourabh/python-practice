fp = open('dypseresult.txt')
lines = fp.read().split('\n')
fp.close()
i = j = k = 0
all_forties = "ENGINEERING MATHEMATICS III      PP    100  40   40"
all_attempted = "ENGINEERING MATHEMATICS III      PP    100  40   "
for x in lines:
 if (x.find("S8088") != -1):
  k += 1
 if (x.find(all_forties) != -1):
  if(x.find("P C",x.find(all_forties)+1) == -1):
   i += 1;
 if (x.find(all_attempted) != -1):
  if(x.find("P C",x.find(all_attempted)+1) != -1):
   j += 1;
print "Total people who passed M3 on 40:",i
print "Cleared in previous attempt:",j
print "Total students with backlogs:", k
print "Students without M3 backlog in May:", k - j


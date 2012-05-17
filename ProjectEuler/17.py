
def count(n):
    w=["null","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty"]
    for i in xrange(0,80):
        w.append("null")
    w[30]="thirty"
    w[40]="forty"
    w[50]="fifty"
    w[60]="sixty"
    w[70]="seventy"
    w[80]="eighty"
    w[90]="ninety"
    s=""
    s=(w[n%10])
    if(n%100<20):
        s=w[n%100]
    elif(n%10==0):
        s=w[((n/10)%10)*10]
    else:
        s=w[((n/10)%10)*10]+s
    if(n%100==0):
        s=w[n/100]+"hundred"
    elif(n%1000>=100):
    	s=w[n/100]+"hundredand"+s
    if(n/1000==1):
        s="onethousand"
    return len(s)

import time
start=time.time()
a=0
for i in range(1,1001):
	a+=count(i)
print a
print "\nElapsed time:",time.time()-start
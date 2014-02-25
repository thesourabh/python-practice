def fact(n):
        if(n>1):
                return n*fact(n-1)
        else:
                return 1
sum=0
for i in range(3,500000):
    copy=i
    total=0
    while(copy>0):
            dig=copy%10
            total+=fact(dig)
            copy/=10
    if(total==i):
            print total
            sum+=total
print "sum: ",sum

#40730

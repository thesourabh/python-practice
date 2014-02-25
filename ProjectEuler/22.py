a=open('names.txt','r')
arr=sorted([wor.strip('"') for wor in a.read().split(',')])
i=0
num=[]
for wo in arr:
        n=0
        i+=1
        n=sum([ord(letter)-64 for letter in wo])
        num.append(n*i)
print sum(num)
a.close()

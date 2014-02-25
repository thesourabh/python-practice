a=open('words.txt','r')
b=a.read()
arr=[]
num=[]
t=[n*(n+1)/2 for n in range(0,30)]
i=0
j=0
word=""
while (i+1<len(b)):
        if(b[i]=='"'):
                if(b[i+1]==','):
                        arr.append(word)
                else:
                        word=""
        elif(b[i]!=','):
                word+=b[i]
        i+=1
i=0
let=0
for wo in arr:
        n=0
        for letter in wo:
                let=ord(letter)-64
                n+=let
        if n in t:
                num.append(n)
print len(num)

a.close()

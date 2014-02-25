pre=[False,False,False,False,False,False,False,False,False,False]
fin = []
total = 0
flag = False

for i in range(1,200):
 for j in range(i+1,2000):
  if (len(str(i)) + len(str(j)) > 5):
   continue
  if (len(str(i)) + len(str(j)) + len(str(i*j)) == 9):
    flag = False
    pre = [False,False,False,False,False,False,False,False,False,False]
    
    si = str(i)
    for k in xrange(0,len(si)):
     if ((pre[int(si[k])] == True) or (si[k] == "0")):
      flag = True
      break
     else:
      pre[int(si[k])] = True
    if flag:
     continue

    sj = str(j)
    for k in xrange(0,len(sj)):
     if ((pre[int(sj[k])] == True) or (sj[k] == "0")):
      flag = True
      break
     else:
      pre[int(sj[k])] = True
    if flag:
     continue

    sij = str(i*j)
    for k in xrange(0,len(sij)):
     if ((pre[int(sij[k])] == True) or (sij[k] == "0")):
      flag = True
      break
     else:
      pre[int(sij[k])] = True
    if flag:
     continue

    
    #total+=i*j
    #print i,"x",j,"=",i*j

    fin.append(i*j)


#print total

ans = sum(list(set(fin)))
print ans

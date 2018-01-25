import sets

def calc(num,start,pre,lis):
 count = 0
 while(start < num):
  copy = num
  st = start
  l = pre
  while copy > 0:
   copy -= st
   if copy < 0:
    copy += st
    if st > 1:
     st -= 1
   elif (copy == 0):
    l += str(st)
    if not (l in lis):
     lis.add(l)
     count += 1 
     if (start > 1) and (num-start > 0):
      count += calc(num - start, 1,pre + str(start),lis)
   else:
    l += str(st)
  start += 1
 return count

num = 30
start = 1
count = calc(num,start,"",set([]))

print "Count: ",count
"""
1 + 1


2 + 1
1 + 1 + 1

3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1
"""
n = 7
k = 50
p = map(int,"1 12 5 111 200 1000 10".strip().split(' '))
count = 0
print k
while k > 0:
    m = min(p)
    for i in xrange(len(p)):
        if (p[i] == m) and (k - p[i] >= 0):
            count += 1
            k -= p[i]
            print count,p[i],k
            del p[i]
            break
    if k <= 0:
        break
print count
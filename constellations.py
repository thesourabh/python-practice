import math

r = open("input.txt", "r").read()
lines = r.split("\n")
index = 0
T = int(lines[index])

ans = ""

for tt in xrange(T):
	index += 1
	num = int(lines[index])
	x = []
	y = []
	for nn in xrange(num):
		index += 1
		starx, stary = map(int, lines[index].split(" "))
		x.append(starx)
		y.append(stary)
	count = 0
	for i in xrange(num):
		for j in xrange(num):
			if (i == j):
				continue
			for k in xrange(num):
				if ((k == i) or (k == j)):
					continue
				d1 = math.sqrt(((x[j] - x[i]) ** 2) + ((y[j] - y[i]) ** 2))
				d2 = math.sqrt(((x[k] - x[j]) ** 2) + ((y[k] - y[j]) ** 2))
				if (d1 == d2):
					count += 1
					#print d1 , "(" , x[i] , "," , y[i] , ") " , "(" , x[j] , "," , y[j] , ") " , "(" , x[k] , "," , y[k] , ") "
	ans += "Case #" + str(tt + 1) + ": " + str(count / 2)
	if (tt < T - 1):
		ans += "\n"
w = open("output.txt", "w")
w.write(ans)
w.close()
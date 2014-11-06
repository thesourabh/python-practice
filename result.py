def isValidRoll(roll):
	if roll == '':
		return 0>1
	return roll[0] == 'S' and not roll[1].isalpha()

fp = open("compo.txt")
a = fp.read()
fp.close()
a = a.split("            ")
import re
allclear = []

for merit in a[0:6]:
	sp = re.split(" |\n\n",merit)
	sp = [i for i in sp if isValidRoll(i)]
	allclear += sp
	#print len(sp)
allclear = sorted(allclear)
coll = []
curr = 0;
stud = 0;
for i in allclear:
	college = int(i[3:5])
	if curr != college:
		coll.append(stud)
		for j in xrange(college-curr-1):
			coll.append(0)
		#print stud
		#print "No.",college,
		curr = college
		stud = 0
	stud+=1
coll.append(stud)
print
print coll


import pylab as p
fig = p.figure()
ax = fig.add_subplot(1,1,1)
x = [i for i in range(len(coll))]
y = coll
ax.set_xticks(x)
ax.tick_params(axis='x', labelsize=8)
ax.bar(x,y)
p.show()

#
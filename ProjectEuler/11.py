fil=open('11.txt')
lines=[]
n=0
for lin in fil:
	lines.append(lin.strip())
	n+=1
nums=[]
for i in range(n):
	nums.append(lines[i].split())

nums= [[int(x) for x in y] for y in nums]

iii=[]
max=1

row=0
r=0
for qwe in nums:
	for i in range(20):
		if((row<=16) & (i>=3)):
			tmp=nums[row][i]*nums[row+1][i-1]*nums[row+2][i-2]*nums[row+3][i-3]
			if (tmp>max):
				max=tmp
				iii=i
				r=row
	row+=1
print r,iii
print nums[r][iii]*nums[r+1][iii-1]*nums[r+2][iii-2]*nums[r+3][iii-3]

#5438256

#1492992

#40304286

#70600674
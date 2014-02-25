day=1
i=1
sunday=0
for year in range(1901,2001):
    for mon in range(1,13):
        if(day==6):
            sunday+=1
        if ((mon==4)|(mon==6)|(mon==9)|(mon==11)):
            lim=30
        elif (mon==2):
            if(year%4==0):
                lim=29
            else:
                lim=28
        else:
            lim=31
        i=0
        while(i<lim):
            day+=1
            if(day==7):
                day=0
            i+=1
print sunday

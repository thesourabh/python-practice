import urllib2

#page = urllib2.urlopen("http://www.imdb.com/name/nm0372176/")
#r = page.read()
page = open("sean.htm","r")
r=page.read()
actstart = r.find('"filmo-head-Actor"')
if(actstart==-1):
    actstart = r.find('"filmo-head-Actress"')
actend = r.find('filmo-head-MiscellaneousCrew"')
if(actend==-1):
    actend = r.find('"filmo-head-Soundtrack"')
if(actend==-1):
    actend = r.find('"filmo-head-Self"')
f=r[actstart:actend]
ystr='<span class="year_column">'
lines = f.split(ystr)
tstr='/rg/name-filmo/title'
li=[]
lines.pop(0)
for line in lines:
    tri=[]
    line=line.replace('&#x27;','\'')
    year=line[:line.find('</span')]
    tri.append(year)
    person=line.split("\n")
    for p in person:
	title=p.find(tstr)
        if(title>=0):
	    t=p[p.find('>')+1:p.find('</a></b>')]
	    url=p[p.find("href=")+6:p.find('>')].strip()
	    tri.append(t)
	    tri.append("http://www.imdb.com"+url[:-1])
	    flag=1
    ch1=line.find('<br/>')
    ch2=line.find('<div class=')
    t=line[ch1:ch2]
    t=t.strip()
    i=0
    flag=0
    s=""
    while(i<len(t)):
	if(t[i]=='<'):
	    flag+=1
	if(t[i]=='>'):
	    flag-=1
	elif(flag==0):
	    if(t[i]!='\n'):
	        s+=t[i]
	i+=1
    s=s.strip()
    tri.append(s)
    li.append(tri)
	

page.close()
page = open("roles.html","w")
start=open("start.ihc","r")
html=start.read()
role=""
for role in li:
    role="<tr><td>"+role[0]+"</td><td><a href='"+role[2]+"'>"+role[1]+"</a></td><td>"+role[3]+"</td></tr>"
    html+=role

html+="</table></body></html>"
page.write(html)

print "\n\n\nOutput saved to file "+page
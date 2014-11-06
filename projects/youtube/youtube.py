import urllib2

def getlinks(url):
	page = urllib2.urlopen(url)
	r = page.read()
	#page = open("you.htm","r")
	#r=page.read()
	title=r[r.find('<title>')+7:r.find('</title>')]
	actstart = r.find('<a href="/watch?v=')
	actend = r.find('< class="tile-link-block video-tile"')
	f=r[actstart:actend]
	ystr='<a href="/watch?v='
	estr='class="tile-link-block video-tile"'
	lines = f.split(estr)
	lines.pop(-1)
	count=0
	
	txtfile=open("links.txt","a")
	txtfile.write(title+'\n')
	for line in lines:
		a=line[line.find(ystr):line.find(estr)]
		b=a[len(ystr)-9:a.find('&amp;list=')]
		b='http://www.youtube.com'+b
		txtfile.write(b+'\n')
		count+=1
		
	print count,"videos in "+title
    

fileclear=open("links.txt","w")
fileclear.write('')
fileclear.close()
getplaylists=open("playlists.txt","r").read()
playlists=getplaylists.split('\n')
for play in playlists:
	getlinks(play)
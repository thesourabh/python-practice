import re
from mechanize import Browser

browser = Browser()
browser2 = Browser()
details=['','','']
sno=8884267
browser.open("http://unipune.ac.in/onlineresult/frmShowResult.aspx")

while(sno<8884268):
	browser.select_form(nr=0)
	browser['cboExamName'] = ['10']
	browser['cboSearchBy'] = ['Seat No']
	strno='s'+str(sno)
	browser['txtSearch'] = strno
	
	response = browser.submit()
	
	content = response.read()
	cont = content.split('<span id="grdColleges_ctl02_')
	result=iter(cont)
	next(result)
	a=0
	for i in result:
		details[a]= i[i.find('">')+2:i.find('</span')]
		a=a+1
	print details[2],details[1],details[0]

	sno+=1
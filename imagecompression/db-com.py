import pymssql
import os
from lxml.html import tostring, html5parser


def cursor2list(cursor):
	try:
		cursor = list(cursor)
		for row in range(0,len(cursor)): 	
			cursor[row] = list(cursor[row])
			for i in range(0,len(cursor[row])): 
		
				try:
					cursor[row][i] = str(cursor[row][i].decode('cp1256'))
				except: 
					print 'error'
			return(cursor)
	except: 
		print "Error in listing "
	
	


home = os.getcwd()
os.chdir('C:/Users/vaibhav.singhal')
print(os.getcwd())

f=open('credentials','r')
f = f.readlines()
credentials = []
for i in f:
	i = i.replace('\n','')
	credentials.append(i)

conn = pymssql.connect(server=credentials[0],user=credentials[1],password=credentials[2],database=credentials[3])

root_list = ['~/aieee/aieee-past-papers/','~/iit-jee-solutions/reverse-osmosis/']

for url in root_list:
	cursor=conn.cursor()
	cursor.execute("""
		SELECT TOP 200 virtualURL,pagecontent
FROM askiiti_askiitians.CMS_PageMaster where pagecontent like '%<img%'""")


	new = cursor2list(cursor)
	print type(new)
# print new
os.chdir(home+'\\htmls')
for i in new :
	f = i[0].split("/")
	fname = f[len(f)-1].split('.')[0]+'.html'
	# print fname
	q = open(fname,'w')
	try:
		q.write((i[1]).decode('cp1256'))
	except:
		print('MISSED: '+ i[0])
	q.close()


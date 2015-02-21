import pymssql
import os


def cursor2list(cursor):
	cursor = list(cursor)
	for row in range(0,len(cursor)): 	
		cursor[row] = list(cursor[row])
		for i in range(0,len(cursor[row])): 
			cursor[row][i] = str(cursor[row][i])
	return(cursor)


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
		SELECT TOP 10 VirtualURL
FROM askiiti_askiitians.CMS_PageMaster""")


	new = cursor2list(cursor)
print new

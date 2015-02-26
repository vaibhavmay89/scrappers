import pymssql
import os

current = os.getcwd()

def cursor2list(cursor):
	cursor = list(cursor)
	for row in range(0,len(cursor)): 	
		cursor[row] = list(cursor[row])
		for i in range(0,len(cursor[row])):
			try: 
				cursor[row][i] = str(cursor[row][i])
			except:
				cursor[row][i] = 'ERROR'
				print('ERROR' + str(i))
	return(cursor)





##########################################################
f = open('template.html','r')

template = f.read()

f = open('data.csv','r')
temp = f.readlines()
# temp = temp[0].split('\n')
for i in range(0,len(temp)):
	temp[i] = temp[i].replace('\n','')



headers = temp[0].split(',')

temp.pop(0)
data = temp

for i in range(0,len(data)):
	data[i] = data[i].split(',')

for i in range(0,len(data)) : 
	t= template
	for j in range(0,len(data[1])):
		t = t.replace('{{'+headers[j]+'}}',data[i][j])
	f = open(str(data[i][0])+".html",'w')
	f.write(str(t))
	f.close()


##################################################################

home = os.getcwd()
os.chdir('C:/Users/vaibhav.singhal')
print(os.getcwd())
# credentials[3]
f=open('credentials','r')
f = f.readlines()
credentials = []
for i in f:
	i = i.replace('\n','')
	credentials.append(i)

conn = pymssql.connect(server=credentials[0],user=credentials[1],password=credentials[2],database="AskIITians_PD_7.4")


###########################################################################
os.chdir(home)
cursor=conn.cursor()
cursor.execute("""
 	SELECT TOP 10 PackageID
FROM askiiti_askiitians.PackageDetail where isactive = 1""")
new = cursor2list(cursor)
cursor.close()

print new

for i in range(0,len(data)):
	j = open(data[i][0]+".html",'r')
	j = j.read()
	print """
	 UPDATE askiiti_askiitians.PackageDetail
SET Description = '"""+j+"""'
Where PackageName Like '%"""+str(data[i][0])+"""%';"""


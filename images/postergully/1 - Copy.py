import requests


import shutil

def getimage(url,fname):
	print(fname)
	response = requests.get(url, stream=True)
	with open('MAXI-'+fname+'.jpg', 'wb') as out_file:
	    shutil.copyfileobj(response.raw, out_file)
	del response


f = open('maxi-posters.txt','r')
final = []
j = f.readlines()
f.close()
for i in range(0,len(j)): 
	j[i]= j[i].replace('//','http://')
	j[i]= j[i].replace('\n','')
	final.append(j[i].split('|',1))
for i in range(0,len(final)):
	getimage(final[i][1],str(i)+'-- Page'+str(final[i][0]))

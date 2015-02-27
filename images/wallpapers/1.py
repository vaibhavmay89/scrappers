import requests


import shutil

def getimage(url):
	f = url.split("/")
	fname = f[len(f)-1]
	print(url)
	response = requests.get(url, stream=True)
	with open(fname, 'wb') as out_file:
	    shutil.copyfileobj(response.raw, out_file)
	del response


f = open('originals.txt','r')
final = []
j = f.readlines()
f.close()
for i in range(0,len(j)): 
	# j[i]= j[i].replace('//','http://')
	j[i]= j[i].replace('\n','')
	final.append(j[i].split('|',1))
for i in range(8000,len(final)):
	print(i)
	getimage(final[i][1],str(i)+'-- Page'+str(final[i][0]))

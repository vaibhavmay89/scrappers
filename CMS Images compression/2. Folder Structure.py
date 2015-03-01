import os 
import shutil
import random 
import requests
# print os.listdir(os.getcwd());
from PIL import Image, ImageFilter
import socket
socket.getaddrinfo('localhost', 8080)

def path(new,mode = 'Images'): 
	global home
	new = new.split('\\')

	directory = home + '\\'+ mode


	for i in new: 
		directory += '\\'+i
		if not os.path.exists(directory):
			os.makedirs(directory)
	return(directory+'\\') 

def getimage(url,fullpath):
	f = url.split("/")
	fname = str(f[len(f)-1])
	# q = open('image.csv','w')
	# q.write(str(fname)+"|"+str(url)+"\n")
	# q.close()
	response = requests.get(url, stream=True)
	with open(fullpath, 'wb') as outfile:
		# print fullpath
		shutil.copyfileobj(response.raw, outfile)
	del response

def getActualDim(image): 
	im = Image.open(image)
	# print(im.size)
	return(im.size)

def convertThumbnail(row,original,oldpath):
	global f,home
	t = os.path.split(f[row][1])
	directory = path(t[0],'Optimized Images')
	im = Image.open(oldpath)
	s = im.size
	ts = [f[row][2],f[row][3]]
	if ts[0] !='NA' and ts[1] != 'NA': 
		compression = [(int(ts[0])*1.0)/s[0],(int(ts[0])*1.0)/s[1]]
		if compression[0]< compression[1]: 
			size = (1000000,ts[1])
		else:
			size = (ts[0],1000000)
	elif ts[0] == 'NA': 
		size = ((1000000,ts[1])) 
	elif ts[1] == 'NA': 
		size = (ts[0],1000000)
	else: 
		size = (ts[0],ts[1])
	im = im.convert('RGB')
	im.thumbnail(size,Image.ANTIALIAS)
	print directory
	try: 
		# home = os.getcwd()
		os.chdir(directory)
		im.save(t[1], "JPEG",quality=50, optimize=True, progressive=True)
		os.chdir(home)
		print 'success: '+ f[row][1]
		return(directory+'\\'+t[1])
		
	except: 
		print 'failed: '+ f[row][1]
		return(oldpath)





f = open('images.csv','r')
f =  f.readlines()
original = []
for i in f: 
	original.append((i.replace('|\n','')).split('|'))
# for i in original: 
# 	print i


####### FOR DIR STRUCTURE #####################
remove = ['http://','.askiitians.com','|\n']
for i in range(0,len(f)):
	for j in remove:
		f[i] = f[i].replace(j,'')
	f[i] = f[i].replace('/','\\')
	f[i] = f[i].split('|')
home = os.getcwd()
finalData = []
qq = open('finalstatus.csv','w')
for i in range(0,len(f)): 
	t = os.path.split(f[i][1])
	directory = path(t[0])
	if f[i][2] != 'NA' or f[i][3] != 'NA': 
		getimage(original[i][1],directory+t[1])
		originalDimentions= getActualDim(directory+t[1])
		originalSize = os.path.getsize(directory+t[1])
		newPath = convertThumbnail(i,originalDimentions,directory+t[1])
		newSize = os.path.getsize(newPath)
		temp = [f[i][0],original[i][1],f[i][1],newPath,originalSize,newSize,(1-newSize/originalSize)*100 ]
		finalData.append(temp)
		for jj in temp: 
			qq = open('finalstatus.csv','a')
			qq.write(str(jj)+'|')
		qq.write('\n')
	else: 
		pass 




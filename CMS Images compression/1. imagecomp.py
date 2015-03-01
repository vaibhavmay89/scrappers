import re 
from lxml import etree
import os 
import PIL
import requests
import shutil
import random 

def getimage(url):
	f = url.split("/")
	fname = str(random.randrange(454534,786885856,3))+"_"+f[len(f)-1]
	q = open('image.csv','w')
	q.write(str(fname)+"|"+str(url)+"\n")
	q.close()

	response = requests.get(url, stream=True)
	with open(fname, 'wb') as out_file:
	    shutil.copyfileobj(response.raw, out_file)
	del response
def parser(row): 
	global imageStats,widthRe,heightRe,width
	e1 = row
	text = imageStats[row][4][0]
	print (text)
	width = int((re.findall(pattern = widthRe,string = text))[0][1])
	height = int(re.findall(pattern = heightRe,string = text)[0][1])
	print height
	return[width,height]
def handler (case,row): 
	global imageStats, widthRe, heightRe
	if case == 8: 
		imageStats[row].append("Perfect")
	if case in [7,5,3,1]:
		# print imageStats[row]
		css = cssparser(row)
		if 'width' in css.keys():
			if '%' not in css['width']:
				imageStats[row][2] = int((re.findall(pattern = widthRe,string = css['width']))[0][1])
		if 'height' in css.keys():
			if '%' not in css['height']:
				imageStats[row][3] = int(re.findall(pattern = heightRe,string = css['height'])[0][1])
		# t = cssparser[row]	
		# imageStats[row][]
		# print imageStats[row][4][0]
		# print("parser required")
		# [imageStats[row][2], imageStats[row][3]] = parser(row)
		
		
	else: 
		pass
		# print("No Parser Needed")
def cssparser(row):
	global imageStats,lastSemiColon
	css = imageStats[row][4][0]
	css = lastSemiColon.sub('',css)
	css = css.split(';')
	for i in range(0,len(css)):
		css[i] = css[i].split(':')
	dic = {}
	for i in css: 
		# print i 
		temp = {i[0]:i[1]}
		dic.update(temp)
	return dic






lastSemiColon = re.compile(r';$')
widthRe = re.compile(r'(\s*)(\d*)(px)',re.I)
heightRe = re.compile(r'(\s*)(\d*)(px)',re.I)

imageStats = [] #[[src,width,height,style],[src,width,height,style]... ]
htmlList = (os.listdir(os.getcwd()+'\\htmls'))
os.chdir(os.getcwd()+'\\htmls')
for i in range(0,len(htmlList)):
	f = open(htmlList[i],'r')
	try:
		tree = etree.HTML(f.read())
	except:
		print("ERROR IN: "+htmlList[i])
		continue;
	totalImages =  len(tree.xpath('//img'))
	# print(totalImages)
	for j in range(0,totalImages): 
		temp = [] 
		temp.append(htmlList[i])
		temp.append(tree.xpath('//img['+str(j+1)+']/@src')[0])
		if len(tree.xpath('//img['+str(j+1)+']/@width')) != 0 : 
			temp.append(int(tree.xpath('//img['+str(j+1)+']/@width')[0]))
		else:
			temp.append('NA')
		if len(tree.xpath('//img['+str(j+1)+']/@height')) != 0 : 
			temp.append(int(tree.xpath('//img['+str(j+1)+']/@height')[0]))
		else:
			temp.append('NA')
		
		
		if len(tree.xpath('//img['+str(j+1)+']/@style')) != 0 : 
			temp.append(tree.xpath('//img['+str(j+1)+']/@style'))
		else:
			temp.append('NA')
		imageStats.append(temp)


for i in range(0,len(imageStats)):
	if imageStats[i][2] != 'NA' and imageStats[i][3] != 'NA' and imageStats[i][4] != 'NA':
		dic = cssparser(i)
		if 'width' in dic.keys() or 'height' in dic.keys(): 
			handler(1,i)
	elif(imageStats[i][2] != 'NA' and imageStats[i][3] != 'NA' and imageStats[i][4] == 'NA'): 
		handler(2,i)
	elif(imageStats[i][2] != 'NA' and imageStats[i][3] == 'NA' and imageStats[i][4] != 'NA'): 
		dic = cssparser(i)
		if 'width' in dic.keys() or 'height' in dic.keys(): 
			handler(3,i)
	elif(imageStats[i][2] != 'NA' and imageStats[i][3] == 'NA' and imageStats[i][4] == 'NA'): 
		handler(4,i)
	elif(imageStats[i][2] == 'NA' and imageStats[i][3] != 'NA' and imageStats[i][4] != 'NA'): 
		dic = cssparser(i)
		if 'width' in dic.keys() or 'height' in dic.keys(): 
			handler(5,i)
	elif(imageStats[i][2] == 'NA' and imageStats[i][3] != 'NA' and imageStats[i][4] == 'NA'): 
		handler(6,i)
	elif(imageStats[i][2] == 'NA' and imageStats[i][3] == 'NA' and imageStats[i][4] != 'NA'): 
		dic = cssparser(i)
		if 'width' in dic.keys() or 'height' in dic.keys(): 
			handler(7,i)
	elif(imageStats[i][2] == 'NA' and imageStats[i][3] == 'NA' and imageStats[i][4] == 'NA'): 
		handler(8,i)



f = open('images.csv','w')
for i in imageStats: 
	for j in range(0,4):
		f.write(str(i[j])+'|')
	f.write('\n')

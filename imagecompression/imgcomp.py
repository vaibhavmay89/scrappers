import re 
from lxml import etree
import os 
import PIL

widthRe = re.compile(r'(width:\s*)(\d*)(px)',re.I)
heightRe = re.compile(r'(height:\s*)(\d*)(px)')

def parser(row): 
	global imageStats,widthRe,heightRe
	text = imageStats[row][4][0]
	print (text)
	width = int((re.findall(pattern = widthRe,string = text))[0][1])
	height = int(re.findall(pattern = heightRe,string = text)[0][1])
	print height
	return[width,height]


def handler (case,row): 
	global imageStats
	if case == 8: 
		imageStats[row].append("Perfect")
	if case == 7:
		# print("parser required")
		[imageStats[row][2], imageStats[row][3]] = parser(row)
		
		
	else: 
		print("No Parser Needed")
	


imageStats = [] #[[src,height,width,style],[src,height,width,style]... ]
htmlList = (os.listdir(os.getcwd()+'\\htmls'))
os.chdir(os.getcwd()+'\\htmls')
for i in range(0,len(htmlList)):
	f = open(htmlList[i],'r')
	tree = etree.HTML(f.read())
	totalImages =  len(tree.xpath('//img'))
	print(totalImages)
	for j in range(0,totalImages): 
		temp = [] 
		temp.append(htmlList[i])
		temp.append(tree.xpath('//img['+str(j+1)+']/@src')[0])
		if len(tree.xpath('//img['+str(j+1)+']/@width')) != 0 : 
			temp.append(tree.xpath('//img['+str(j+1)+']/@width'))
		else:
			temp.append('NA')
		if len(tree.xpath('//img['+str(j+1)+']/@height')) != 0 : 
			temp.append(tree.xpath('//img['+str(j+1)+']/@height'))
		else:
			temp.append('NA')
		
		
		if len(tree.xpath('//img['+str(j+1)+']/@style')) != 0 : 
			temp.append(tree.xpath('//img['+str(j+1)+']/@style'))
		else:
			temp.append('NA')
		imageStats.append(temp)

print ("----------------------------------------------------")

for i in range(0,len(imageStats)):
	if imageStats[i][2] != 'NA' and imageStats[i][3] != 'NA' and imageStats[4] != 'NA':
		handler(1,i)
	elif(imageStats[i][2] != 'NA' and imageStats[i][3] != 'NA' and imageStats[4] == 'NA'): 
		handler(2,i)
	elif(imageStats[i][2] != 'NA' and imageStats[i][3] == 'NA' and imageStats[4] != 'NA'): 
		handler(3,i)
	elif(imageStats[i][2] != 'NA' and imageStats[i][3] == 'NA' and imageStats[4] == 'NA'): 
		handler(4,i)
	elif(imageStats[i][2] == 'NA' and imageStats[i][3] != 'NA' and imageStats[4] != 'NA'): 
		handler(5,i)
	elif(imageStats[i][2] == 'NA' and imageStats[i][3] != 'NA' and imageStats[4] == 'NA'): 
		handler(6,i)
	elif(imageStats[i][2] == 'NA' and imageStats[i][3] == 'NA' and imageStats[4] != 'NA'): 
		handler(7,i)
	elif(imageStats[i][2] == 'NA' and imageStats[i][3] == 'NA' and imageStats[4] == 'NA'): 
		handler(8,i)
	




for i in imageStats: 
	print (i[2:4])
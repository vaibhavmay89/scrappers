import os 
from lxml import etree
import requests
import shutil

def getimage(url,fname):
	try:
		print(fname)
	except: 
		print 'unicode error in the fname '
	response = requests.get(url, stream=True)
	with open(fname, 'wb') as out_file:
	    shutil.copyfileobj(response.raw, out_file)
	del response


#home sweet home
current = os.getcwd()
# switching to the source 
os.chdir(current+r'\htmls')

fileList = os.listdir(os.getcwd())
htmlList = []
for i in range(0,len(fileList)):
	if ".html"  in fileList[i]:
		htmlList.append(fileList[i])

hlmlFiles = []
# getting just the HTMLS Files
for i in htmlList: 
	f = open(i,'r')
	h = f.read()
	hlmlFiles.append([i,h])
	f.close()


#Downloading all the images
os.chdir(current+r'\htmls-new'+r'\images')
imageList = []
for i in hlmlFiles:
	tree = etree.HTML(i[1])
	# tree 
	imagesOnThisPage = tree.xpath("//img/@src")
	try:
		for j in imagesOnThisPage: 
			## List and download to images folder 
			## Repalce the name in text 
			fname = j.split('/')[-1]
			i[1]=i[1].replace(j,"images/"+fname)
			getimage(j,fname)
		# writing the updated html file ... 

		os.chdir(current+r'\htmls-new')
		newHtml = i[1]
		f = open(i[0],'w')
		f.write(i[1])
		f.close()
		os.chdir(current+r'\htmls-new'+r'\images')
	except: 
		print 'Skipping file: '+ i[0]
	








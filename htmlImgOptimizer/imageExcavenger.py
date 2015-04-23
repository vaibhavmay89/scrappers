import os,requests
from lxml import etree




def checkOrCreateImagePath(url):

	pass 



def downloadImage(url):


	checkOrCreateImagePath(url)
	# save Image 
	pass 


current = os.getcwd()

htmls = current+'\\html'
os.chdir(htmls)

htmlFileNameList = os.listdir(htmls);

images = []
for i in htmlFileNameList : 
	f = open(i,'r')
	text = f.read()
	tree = etree.HTML(text) 
	imageCDNPathList = tree.xpath('//img/@src')
	for ii in imageCDNPathList: 
		downloadImage(ii)
		images.append(ii)


for i in images: 
	try: 
		print i 
	except: 
		print 'error'
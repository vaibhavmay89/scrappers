import requests
from lxml import html
imgURL = []

f = open('hacks.txt','w')
for i in range(1,118):
	url = 'http://thelisticles.net/life-hacks-that-make-life-easier/531364/'+str(i)+"/"
	page  = requests.get(url)
	tree = html.fromstring(page.text)
	response = (tree.xpath('//img/@src'))
	for img in response:
		imgURL.append([img,i])
		print(img)
		f.write(str(i)+'|'+str(img)+'\n')
	print(i)






# //div[@class='main']/a/img/@src

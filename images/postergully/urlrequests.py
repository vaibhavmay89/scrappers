import requests
from lxml import html
imgURL = []

f = open('maxi-posters.txt','w')
for i in range(1,118):
	url = 'http://www.postergully.com/collections/maxi-posters?page='+str(i)
	page  = requests.get(url)
	tree = html.fromstring(page.text)
	response = (tree.xpath('//div[@class="main"]/a/img/@src'))
	for img in response:
		imgURL.append([img,i])
		f.write(str(i)+'|'+str(img)+'\n')
	print(i)






# //div[@class='main']/a/img/@src

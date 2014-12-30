import requests
from lxml import html
imgURL = []

f = open('hacks.txt','w')
for i in range(1,800):
	url = 'http://www.hdwallpapers.in/top_download_wallpapers/page/'+str(i)
	page  = requests.get(url)
	tree = html.fromstring(page.text)
	response = (tree.xpath("//div[@class='thumbbg']/div[@class='thumb']/a/@href"))
	for img in response:
		imgURL.append([img,i])
		print(img)
		f.write(str(i)+'|'+str(img)+'\n')
	print(i)






# //div[@class='main']/a/img/@src

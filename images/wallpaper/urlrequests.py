import requests
from lxml import html
imgURL = []

f = open('wallpapers.txt','w')
for i in range(1,118):
	url = 'http://wallfinest.com/best-wallpapers/page/'+str(i)+'/'
	page  = requests.get(url)
	tree = html.fromstring(page.text)
	response = (tree.xpath('//h2/a/@href'))
	for img in response:
		print (img)
		ip = requests.get(img)
		it = html.fromstring(ip.text)
		image = tree.xpath("//img/@src")
		# print(image)
		for ii in image:
			f.write(str(ii)+'\n')
	print(i)






# //div[@class='main']/a/img/@src
# //div[@class='post-content description']/p/img[@class='attachment-full no-display appear']/@src
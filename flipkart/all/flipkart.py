import requests
from lxml import html
import requests 


f = open('urls.txt','r', encoding= 'utf8')
urls = f.readlines()



dict = {
	'name': '//h1/text()',
	'ImageURL': "//img[@class='productImage current']/@src",
	'cost': "//span[@class='selling-price omniture-field']/text()",
	# 'phone' : "//div[@id='phoneNoString']/div/span/span/span/text()",
	# 'highlight': "//div[@class='res-info-feature-text']/text()",
	# "locality":'//span[@itemprop="addressLocality"]/text()',
	# "address": '//h2[@itemprop="address"]/text()',
	"ratings":"//div[@class='bigStar']/text()",
	"votes":"//div[@class='ratings']/div[@class='count']/span/text()",
	"noReviews": "//div[@class='reviews']/a[@class='review']/span/text()",
	"speckey": "//td[@class='specsKey']/text()",
	"specvalue": "//td[@class='specsValue']/text()"
}


f = open('full_list.txt','a', encoding= 'utf8')
full = []
l = []
for i in range(146,len(urls)): 
	urls[i] = urls[i].replace("\n","")
	page  = requests.get(urls[i])
	tree = html.fromstring(page.text)
	for key in dict: 
		
		l.append(tree.xpath(dict[key]))
		full.append
	try:
		
		f.write("'"+str(i)+"',"+str(l)+'\n||||')
	except:
		print ("Decode error")
	l = []
	print (i)


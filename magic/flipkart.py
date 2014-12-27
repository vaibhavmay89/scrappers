import requests
from lxml import html
import requests 


f = open('urls.txt','r', encoding= 'utf8')
urls = f.readlines()



dict = {
	'name': "//div[@class='propPriceBrief']/div[@class='fHeading']/text()",
	# 'ImageURL': "//img[@class='productImage current']/@src",
	'cost': '//*[@id="propDPaage"]/div[2]/div[2]/div[1]/div/div[4]/text()',
	# 'phone' : "//div[@id='phoneNoString']/div/span/span/span/text()",
	# 'highlight': "//div[@class='res-info-feature-text']/text()",
	# "locality":'//span[@itemprop="addressLocality"]/text()',
	# "address": '//h2[@itemprop="address"]/text()',
	"date":"//div[@class='propertyBrief']/div[@class='briefRight']/div[@class='propDenId']/text()",
	"trends":"//div[@class='currentSalesPrice']/ul/li/span/text()",
	"amenities": "//div[@class='animList']/ul/li/text()",
	"speckey": "//div[@class='listBlock']/div[@class='fieldLabel']/text()",
	"specvalue": "//div[@class='listBlock'][9]/div[@class='fieldVal']/text()"
}


f = open('full_list.txt','a', encoding= 'utf8')
full = []
l = []
for i in range(0,len(urls)): 
	urls[i] = urls[i].replace("\n","")
	page  = requests.get(urls[i])
	tree = html.fromstring(page.text)
	for key in dict: 
		print(key)
		l.append(tree.xpath(dict[key]))
		full.append
	try:
		print(str(l))
		f.write("'"+str(i)+"',"+str(l)+'\n||||')
	except:
		print ("Decode error")
	l = []
	print (i)


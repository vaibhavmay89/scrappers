import requests
from lxml import html
import requests 


f = open('urls.txt','r')
urls = f.readlines()



dict = {
	'name': '//h1/a/span/text()',
	'time': "//span[@class='res-info-timings']/div/div/div/span/text()",
	'cost': '//span[@itemprop="priceRange"]/text()',
	'phone' : "//div[@id='phoneNoString']/div/span/span/span/text()",
	'highlight': "//div[@class='res-info-feature-text']/text()",
	"locality":'//span[@itemprop="addressLocality"]/text()',
	"address": '//h2[@itemprop="address"]/text()',
	"ratings":"//div[@class='rating-for-2331 rating-div small-rating rrw-aggregate level-6']/text()",
	"votes":"//span[@class='tooltip_formatted fbold']/span/text()",
	"noReviews": "//a[@class='default-section-title everyone empty']/span/text()"
}


f = open('full_list.txt','a')

l = []
for i in range(0,len(urls)): 
	urls[i] = urls[i].replace("\n","")
	page  = requests.get(urls[i])
	tree = html.fromstring(page.text)
	for key in dict: 
		##print(key)
		l.append(tree.xpath(dict[key]))
	print(str(l))
	f.write("'"+str(i)+"',"+str(l)+'\n||||')
	l = []
	print (i)



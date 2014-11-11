import requests
from lxml import html
import requests 


f = open('urls.txt','r')# encoding= 'utf8')
urls = f.readlines()

def clean(s):
	junk = ['\\n','\\t','\t']
	for k in junk: 
		s = s.replace(k,'')
	while("  " in s) :
		s = s.replace("  "," ")
	return(s)





dict = {
	'name': '//h1/text()',
	'ImageURL': "//img[@class='productImage  current']/@src",
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
keys = []
rec = []
for key in dict: 
	rec.append(dict[key])
	keys.append(key)
print(keys)
f = open('full_list.py','a')# encoding= 'utf8')
f.write('#'+str(keys))
f.write('\nfull = []\n')
full = []
l = []
for i in range(0,len(urls)): 
	urls[i] = urls[i].replace("\n","")
	page  = requests.get(urls[i])
	tree = html.fromstring(page.text)
	for key in range(0,len(rec)): 
		try:
			l.append(tree.xpath(rec[key]))
		except:
			l.append([str(key) + "  - N/A"])
		full.append
	try:
		s = str(l)
		s = clean(s)
		#print (s)
		f.write("\nfull.append("+s+")")
	except:
		print ("Decode error")
	l = []
	print (i)


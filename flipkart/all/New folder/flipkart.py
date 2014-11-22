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
	"discount": "//span[@class='discount fk-green']/text()",
	"originalPrice": "//span[@class='price list']/text()",
	"ratings":"//div[@class='bigStar']/text()",
	"votes":"//div[@class='ratings']/div[@class='count']/span/text()",
	"noReviews": "//div[@class='reviews']/a[@class='review']/span/text()",
	"speckey": "//td[@class='specsKey']/text()",
	"specvalue": "//td[@class='specsValue']/text()"
}
keys = []
rec = []
rec.append(dict['name'])
rec.append(dict['cost'])
rec.append(dict["discount"])
rec.append(dict["originalPrice"])
rec.append(dict["ratings"])
rec.append(dict["noReviews"])
rec.append(dict["votes"])
rec.append(dict["speckey"])
rec.append(dict["specvalue"])
rec.append(dict['ImageURL'])

f = open('full_list.py','a')# encoding= 'utf8')
f.write('#'+str(keys))
f.write('\nfull = []\n')
full = []
l = []
for i in range(0,7): 
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

s = """

#[ 'name',  'cost',  "discount",  "originalPrice",  "ratings",  "noReviews",  "votes",  "speckey",  "specvalue",  'ImageURL' ]

specs = []
filter = 0 
for i in range (0,len(full)):
	for j in range(0,len(full[i][7])):
		if full[i][7][j] in specs:
			filter +=1
			continue
			
		else:

			specs.append(full[i][7][j])

for i in specs: 
	print (i)
print(str(len(specs)) +"    "+str(filter))


### NAME , Brand , PRICE , specs , 
###	for i in range(0,len(full[0])):
###	print(str(i)+":   "+str(full[0][i]))

new = []

for i in range (0,len(full)):
	new.append([full[i][0], full[i][1], full[i][2], full[i][3], full[i][4], full[i][5], full[i][6]])
	for j in range(0,len(full[i][7])):
		for k in range(0,len(specs)) :
			try:
				#print("found one")
				index = full[i][7].index(specs[k])
				new[i].append(full[i][8][index])
				#print(str(i)+ ":   "+ full[i][8][index])
			except:
				new[i].append("N/A")


# building header
t = ''
for s in specs: 
	t += s+ "|"

f = open("final.csv","a")
f.write('"name"|"cost"|"discount"|"originalPrice"|"ratings"|"noReviews"|"votes"|"speckey"|"specvalue"|"ImageURL"')


for i in range(0,len(new)):
	f.write("\\n")
	for j in new[i]:
		#print(j)
		f.write(str(j)+"|")
# for row in new: 
# 	f.write("\\n"+ str(row))



"""
print("Hmmm... Got the data! .. digestion required. Autowriting the code")

f.write(s)

import full_list
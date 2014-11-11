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
,	"ratings":"//div[@class='bigStar']/text()",
	"votes":"//div[@class='ratings']/div[@class='count']/span/text()",
	"noReviews": "//div[@class='reviews']/a[@class='review']/span/text()",
	"speckey": "//td[@class='specsKey']/text()",
	"specvalue": "//td[@class='specsValue']/text()"
}
keys = []
rec = []
rec[0] = dict['name']
rec[1] = dict['cost']
rec[2] = dict["discount"]
rec[3] = dict["originalPrice"]
rec[4] = dict["ratings"]
rec[4] = dict["noReviews"]
rec[5] = dict["votes"]
rec[6] = dict["speckey"]
rec[7] = dict["specvalue"]
rec[8] = dict['ImageURL']

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

s = """


#['ImageURL', 'noReviews', 'votes', 'ratings', 'speckey', 'specvalue', 'cost', 'name']

specs = []
filter = 0 
for i in range (0,len(full)):
	for j in range(0,len(full[i][4])):
		if full[i][4][j] in specs:
			filter +=1
			continue
			
		else:
			specs.append(full[i][4][j])

for i in specs: 
	print (i)
print(str(len(specs)) +"    "+str(filter))


### NAME , Brand , PRICE , specs , 

# for i in range(0,len(full[0])):
# 	print(str(i)+":   "+str(full[0][i]))
new = []

for i in range (0,len(full)):
	new.append([full[i][7], full[i][6], full[i][3], full[i][2], full[i][1]])
	for j in range(0,len(full[i][4])):
		for k in range(0,len(specs)) :
			try:
				#print("found one")
				index = full[i][4].index(specs[k])
				new[i].append(full[i][5][index])
				#print(str(i)+ ":   "+ full[i][1][index])
			except:
				new[i].append("N/A")


# building header
t = ''
for s in specs: 
	t += s+ "|"

f = open("final.txt","a")
f.write("name|"+"Price|"+"Raiting|"+"Votes|"+"5|"+"3|"+ t)


for i in range(0,len(new)):
	f.write("\n")
	for j in new[i]:
		#print(j)
		f.write(str(j)+"|")
# for row in new: 
# 	f.write("\n"+ str(row))



"""
print("Hmmm... Got the data! .. digestion required. Autowriting the digestion code")

f.write(s)


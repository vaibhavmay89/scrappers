from lxml import etree
import requests


f = open('urls.txt','r')# encoding= 'utf8')
urls = f.readlines()
for i in range(0,len(urls)):
	urls[i] = urls[i].replace('\n','')


def tester(st):
	remove = ['\n','"',",","[","]"," ","'","\\n"]
	for i in remove:
		while i in st:
			st = st.replace(i,'')
	return(len(st))

def valkey(tree):

	p = tree.xpath("//div[@class='fieldLabel']")
	key = []
	val = []
	# print(len(p))
	for i in range(0,len(p)):
		key.append(tree.xpath("//div[@class='listBlock']["+str(i+1)+"]/div[@class='fieldLabel']/text()"))
		t = tree.xpath("//div[@class='listBlock']["+str(i+1)+"]/div[@class='fieldVal']/text()")
		if tester(str(t)) == 0: 
			t = tree.xpath("//div[@class='listBlock']["+str(i+1)+"]/span[@class='fieldVal']/span[@id='coveredAreaDisplay']/text()")
			# print("covered area" + str(tester(t)))
			if tester(t) == 0: 
				t = tree.xpath("//div[@class='listBlock']["+str(i+1)+"]/div[@class='fieldVal']/span[@id='carpetAreaDisplay']/text()")
				# print("carpet area = " + str(t))
				if tester(t) == 0: 					
					t = tree.xpath("//div[@class='listBlock']["+str(i+1)+"]/div[@class='fieldVal']/span[@id='plotAreaDisplay']/text()")
					print("//div[@class='listBlock']["+str(i+1)+"]/div[@class='fieldVal']/span[@id='plotAreaDisplay']/text()") 
					if tester(t) == 0 :
						print("Couldnt Find =>  "+str(tree.xpath("//div[@class='listBlock']["+str(i+1)+"]/div[@class='fieldLabel']/text()")))
						val.append("MISSED")
					else:
						val.append(t)
				else:
					val.append(t)
			else:
				val.append(t)
		else:
			val.append(t)


	return(key,val)







def clean(s):
	junk = ['\\n','\\t','\t']
	for k in junk: 
		s = s.replace(k,'')
	while("  " in s) :
		s = s.replace("  "," ")
	return(s)
dict = {
	'name': "//div[@class='propPriceBrief']/div[@class='fHeading']/text()",
	'cost': '//*[@id="propDPaage"]/div[2]/div[2]/div[1]/div/div[4]/text()[2]',
	"persqft": '//*[@id="propDPaage"]/div[2]/div[2]/div[1]/div/div[4]/span[2]/text()[2]',
	"trend": '//*[@id="propDPaage"]/div[2]/div[2]/div[1]/div/div[4]/span[3]/text()[1]',
	"date": '//*[@id="propDPaage"]/div[2]/div[1]/div[2]/div/text()[1]',
	#"trends":"//div[@class='currentSalesPrice']/ul/li/span/text()",
	"amenities": "//div[@class='animList']/ul/li/text()",
	# "speckey": "//div[@class='listBlock']/div[@class='fieldLabel']/text()",
	# "specvalue": "//div[@class='listBlock']/div[@class='fieldVal']/text()",
	# "specvalue2": "//div[@class='listBlock']/div[@class='fieldVal']/span/text()"
}
rec = []
rec.append(dict['name'])
rec.append(dict['cost'])
rec.append(dict['persqft'])
rec.append(dict['trend'])
rec.append(dict["date"])
# rec.append(dict["trends"])
rec.append(dict["amenities"])
# rec.append(dict["speckey"])
# rec.append(dict["specvalue"])
# rec.append(dict["specvalue2"])
raw_data = []

f = open('raw data2.py','w')
f.write("full = [] \n\n\n\n\n")
f.close()
print(len(urls))
for i in range(0,len(urls)):
	print(i)
	raw_data.append([i+1,urls[i]])
	page = requests.get(urls[i])
	tree = etree.HTML(page.text)
	for key in rec:
		# print(key)
		raw_data[0].append(tree.xpath(key))
	t = valkey(tree)
	raw_data[0].append(t[0])
	raw_data[0].append(t[1])

	f = open('raw data2.py','a')
	f.write("full.append("+str(raw_data[0])+")\n")
	f.close()
	raw_data = []


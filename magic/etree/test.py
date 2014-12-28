from lxml import etree
import requests


url = 'http://www.magicbricks.com/propertyDetails/3-BHK-700-Sq-ft-Builder-Floor-Apartment-FOR-Sale-Uttam-Nagar-in-New-Delhi&id=ZtgMMpzJap5zpSvf+uAgZw=='
def tester(st):
	remove = ['\n','"',",","[","]"," ","'","\\n"]
	for i in remove:
		while i in st:
			st = st.replace(i,'')
	return(len(st))

requests.get(url)
page = requests.get(url)
tree = etree.HTML(page.text)
p = tree.xpath("//div[@class='fieldLabel']")
key = []
val = []
print(len(p))
for i in range(0,len(p)):
	key.append(tree.xpath("//div[@class='listBlock']["+str(i+1)+"]/div[@class='fieldLabel']/text()"))
	t = tree.xpath("//div[@class='listBlock']["+str(i+1)+"]/div[@class='fieldVal']/text()")
	if tester(str(t)) == 0: 
		t = tree.xpath("//div[@class='listBlock']["+str(i+1)+"]/span[@class='fieldVal']/span[@id='coveredAreaDisplay']/text()")
		print("covered area" + str(tester(t)))
		if tester(t) == 0: 
			t = tree.xpath("//div[@class='listBlock']["+str(i+1)+"]/div[@class='fieldVal']/span[@id='carpetAreaDisplay']/text()")
			print("carpet area = " + str(t))
			if tester(t) == 0: 
				print("Couldnt Find =>  "+str(tree.xpath("//div[@class='listBlock']["+str(i+1)+"]/div[@class='fieldLabel']/text()")))
				val.append("MISSED")
			else:
				val.append(t)
		else:
			val.append(t)
	else:
		val.append(t)



for i in range(0,len(val)):
	print(str(key[i])+"-----"+str(val[i]) + "----"+str(tester(str(val[i]))))
	# str(key[i])+"-----"+str(val[i]) + "----"+


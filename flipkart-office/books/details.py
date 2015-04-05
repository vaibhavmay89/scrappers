from lxml import etree
import requests


f = open('urls.txt','r')
data = f.readlines()
for i in range(0,len(data)): 
	data[i].replace('\n','')
dictionary = {"title": "//h1[@class='title']/text()",
"img": "//img[@class='productImage  current']/@data-src",
"content": "//div[@class='description-text']/child::text()",
"specKe": "//td[@class='specsKey']/text()",
"specVal": "//td[@class='specsValue']/text()",
"rating": "//div[@class='bigStar']/text()",
"votes": "/div[@class='avgWrapper']/p[@class='subText'][2]/text()",
"seller":"//a[@class='seller-name']/text()"}

data[0]="http://www.flipkart.com/arise-awake-inspiring-stories-10-young-entrepreneurs-graduated-college-into-business-their-own-english/p/itme2t5pwafxk89z?pid=9789384030872&srno=b_22&al=VI9czj2bJnJxYedXS8L%2F%2BEnkC21x8Z0xfK22ySJx2hDeRU2nCHYdZoaLq2lx4bRfFLwHQxVDMNU%3D&ref=f6269a16-603c-4b01-879c-f93c892c47f1"
print data[0]
page = requests.get(data[0],stream=True)
print page.status_code
tree = etree.HTML(page.text)
# print page.text
replace = ['\\xa0','\r','\n','\\t',"u'",'"',"\\n","\\r","'"]
for key in dictionary: 
	t = tree.xpath(dictionary[key])
	for jj in replace: 
		t = str(t).replace(jj,' ')
		pass
	print key+'\t\t: \t'+(((str(t)).replace('\n','')).replace('  ','')).replace(' ,',',')






# for i in range(0,len(urls)) : 
# 	page = requests.get(url[i])
# 	tree = etree.HTML(page.text)
# 	t =  tree.xpath(key)
# 	f=open('urls.txt','a')
# 	print str(len(t)*ii)
# 	ii+=1
# 	for j in t: 

# 		f.write('http://www.flipkart.com'+j+'\n')
# 	f.close()



from lxml import etree
import requests

# 41

key = "//a[@class='lu-title']/@href"

f = open('urls.txt','w')
f.close()
for i in range(0,300) : 
	page = requests.get('http://www.flipkart.com/lc/pr/pv1/spotList1/spot1/productList?sid=bks%2Cenp%2Cuhu%2C50s&filterNone=true&start='+str(i*20)+'&ajax=true&_=1427910340713')
	tree = etree.HTML(page.text)
	t =  tree.xpath(key)
	f=open('urls.txt','a')
	print str(len(t)*i)
	for j in t: 

		f.write('http://www.flipkart.com'+j+'\n')
	f.close()



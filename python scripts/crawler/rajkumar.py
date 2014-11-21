from lxml import html
import requests 
import time 
import csv
from lxml import etree

urls = ["http://rajkumarbiology.weebly.com/class-11-chap-1.html",
"http://rajkumarbiology.weebly.com/class-11-chap-2.html",
"http://rajkumarbiology.weebly.com/class-11-chap-3.html",
"http://rajkumarbiology.weebly.com/class-11-chap-4.html",
"http://rajkumarbiology.weebly.com/class-11-chap-5.html",
"http://rajkumarbiology.weebly.com/class-11-chap-6.html",
"http://rajkumarbiology.weebly.com/class-11-chap-7.html",
"http://rajkumarbiology.weebly.com/class-11-chap-8.html",
"http://rajkumarbiology.weebly.com/class-11-chap-9.html",
"http://rajkumarbiology.weebly.com/class-11-chap-10.html",
"http://rajkumarbiology.weebly.com/class-11-chap-11.html",
"http://rajkumarbiology.weebly.com/class-11-chap-12.html",
"http://rajkumarbiology.weebly.com/class-11-chap-13.html",
"http://rajkumarbiology.weebly.com/class-11-chap-14.html",
"http://rajkumarbiology.weebly.com/class-11-chap-15.html",
"http://rajkumarbiology.weebly.com/class-11-chap-16.html",
"http://rajkumarbiology.weebly.com/class-11-chap-17.html",
"http://rajkumarbiology.weebly.com/class-11-chap-18.html",
"http://rajkumarbiology.weebly.com/class-11-chap-19.html",
"http://rajkumarbiology.weebly.com/class-11-chap-20.html",
"http://rajkumarbiology.weebly.com/class-11-chap-21.html",
"http://rajkumarbiology.weebly.com/class-11-chap-22.html",
"http://rajkumarbiology.weebly.com/chapter-1.html",
"http://rajkumarbiology.weebly.com/chapter-2.html",
"http://rajkumarbiology.weebly.com/chapter-3.html",
"http://rajkumarbiology.weebly.com/chapter-4.html",
"http://rajkumarbiology.weebly.com/chapter-5.html",
"http://rajkumarbiology.weebly.com/chapter-6.html",
"http://rajkumarbiology.weebly.com/chapter-7.html",
"http://rajkumarbiology.weebly.com/chapter-8.html",
"http://rajkumarbiology.weebly.com/chapter-9.html",
"http://rajkumarbiology.weebly.com/chapter-10.html",
"http://rajkumarbiology.weebly.com/chapter-11.html",
"http://rajkumarbiology.weebly.com/chapter-12.html",
"http://rajkumarbiology.weebly.com/chapter-13.html",
"http://rajkumarbiology.weebly.com/chapter-14.html",
"http://rajkumarbiology.weebly.com/chapter-15.html",
"http://rajkumarbiology.weebly.com/chapter-16.html",]

p= []
i = 0
for url in urls: 
	i=i+1
	print("\n\n++++++++++++++++++\n\t\t"+str(i)+"\n\n++++++++++++++++++\n\t\t")
	page = requests.get(str(url))
	tree = html.fromstring(page.text)
	for elem in tree.xpath("//div[@id='content']"):
		print etree.tostring(elem, pretty_print=True)
		print('----------------------------')
	#print(tree.xpath("//div[@id='content']/node()"))
	print ("===================")
	p.append(["@@@"+url+"|||"+etree.tostring(elem, pretty_print=True)+"~~~"])

print p
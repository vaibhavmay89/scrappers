from lxml import etree
import requests


f = open('urlsflip.txt','r')# encoding= 'utf8')
urls = f.readlines()
for i in range(0,len(urls)):
	urls[i] = urls[i].replace('\n','')





for i in range(0,len(urls)):
	print(i)
	raw_data.append([i+1,urls[i]])
	page = requests.get(urls[i])	
	raw_data[0].append(tree.xpath(key))  
	raw_data[0].append(t[0])
	raw_data[0].append(t[1])

	f = open('raw data2.py','a')
	f.write("full.append("+str(raw_data[0])+")\n")
	f.close()
	raw_data = []

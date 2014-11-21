
from lxml import html
import requests 
import time 
import csv
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
p = []
for page_no in range(0,len(alpha)):

	# STACK EXCHANGE
	url = "http://math.stackexchange.com/tags?page="+str(page_no)
	print(url)
	page = requests.get(str(url))
	tree = html.fromstring(page.text)
	p.append(tree.xpath("//a[@class='post-tag']/text()"))
	print (p)
	


	url = "http://www.cut-the-knot.org/glossary/"+alpha[page_no]+"top.shtml"
	print(url)
	page = requests.get(str(url))
	tree = html.fromstring(page.text)
	p.append(tree.xpath("//div[@class='mainFrame']/ul/li/a/text()"))
	print (p)


	url = "http://www2.estrellamountain.edu/faculty/farabee/BIOBK/BioBookgloss"+alpha[page_no]+".html"
	print(url)
	page = requests.get(str(url))
	tree = html.fromstring(page.text)
	p.append(tree.xpath("//p/font/b/text()"))
	print (p)
	
	url = "http://www.ucmp.berkeley.edu/glossary/glossary_"+alpha[page_no].upper()+".html"
	print(url)
	page = requests.get(str(url))
	tree = html.fromstring(page.text)
	p.append(tree.xpath("//p/strong/text()"))
	
	

	url = "http://www.phschool.com/science/biology_place/glossary/"+alpha[page_no]+".html"
	print(url)
	page = requests.get(str(url))
	tree = html.fromstring(page.text)
	p.append(tree.xpath("//p/strong/text()"))




	print(str(p).count(',')+1)



print (p)

	

# ##
# reqn = 0 
	#page = requests.get('https://dl.dropboxusercontent.com/u/7333305/test.html')
# missedlist = []
# def writefile(filename,text):
# 	file = open(filename,"a")
# 	file.write("\n")
# 	try:
# 		file.write(text)
# 	except:
# 		printer("UNABLE TO WRITE !")
# 		file.write("-------- MISSED SOMETHING HERE !! ---------------------------")
# 		file.close()
# 		pass


# def printer(string):
# 	print(string)
# 	writefile("logsSelNR.txt",string)

# def openurl(url): 
# 	global reqn
# 	time.sleep(2)
# 	reqn +=1
# 	printer (str(reqn) + " Requests made so far!")
# 	page = requests.get(str(url))
# 	printer (str(reqn) + " Requests made so far!" + str(page.status_code))
# 	#page = requests.get('https://dl.dropboxusercontent.com/u/7333305/test.html')
# 	tree = html.fromstring(page.text)
# 	return tree

# data = []
# file = open('data.txt','r')
# lines = file.readlines()
# print(type(lines))
# for line in lines:
# 	line.replace('\n','')
# 	data.append(line)

# list1= []

# url = 'http://www.sciencedirect.com/science/article/pii/S1359645414005989?np=y'
# for di in range(0,len(data)):
#         tree = 0
#         p = data[di].replace("\n","")
#         p = p.strip()
#         print(p)
#         tree = openurl(data[di])
#         author_list = tree.xpath('//li/a[@class = "authorName S_C_authorName"]/text()')
#         print(tree.xpath("//div[@class='title']/a[@class='cLink']/span/text()"))
#         #if len(author_list) >=1: 
#         print ("paper title:" + str(tree.xpath("//h1[@class = 'svTitle']/text()")))
#         print ("Journal Name: " + str(tree.xpath("//div[@class='title']/a[@class='cLink']/span/text()")))
#         print("authors" + str(tree.xpath('//li/a[@class = "authorName S_C_authorName"]/text()')))
#         print("\n\nAbstract" + str(tree.xpath("//p[@id='sp0005']")) +"\n\n")
#         paperTitle = str(tree.xpath("//h1[@class = 'svTitle']/text()"))
#         journal = str(tree.xpath("//div[@class='title']/a[@class='cLink']/span/text()"))
#         authors = tree.xpath('//li/a[@class = "authorName S_C_authorName"]/text()')
#         abstract = str(tree.xpath("//p[@id='sp0005']/text()"))
#         try:
#                 emails = tree.xpath("//li/a[@class='auth_mail']/@href")
#                 list1.append([url,paperTitle,journal,authors,emails])
#         except:
#                 print("none has a valid email")
# ##                missedlist.append(url)
# ##                print("missed may be an index page!")
# #continue
# print(list1)

# #Paper Name 						= tree.xpath("//h1[@class = 'svTitle']/text()")
# #list of authors 					= tree.xpath('//ul[@class = "authorGroup noCollab"]/li')
# # Journal Name 						= tree.xpath('//div[@class="title"]')
# #list of mails AN author 			= tree.xpath('//li[3]/a[@class = "auth_mail"]/@href')
# #abstract 							= tree.xpath("//p[@id='sp0005']")

# ############## IMPORTING DATA ##################
# Status API Training Shop Blog About
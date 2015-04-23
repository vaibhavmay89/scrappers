from lxml import etree
import requests

# 41
urls = [
'http://www.flipkart.com/books/educational-and-professional/entrance-exams-preparation/pr?p%5B%5D=facets.exams%255B%255D%3DAIIMS&p%5B%5D=facets.exams%255B%255D%3DCBSE&p%5B%5D=facets.exams%255B%255D%3DCBSE%2B-%2BAIPMT&p%5B%5D=facets.exams%255B%255D%3DJEE&p%5B%5D=facets.exams%255B%255D%3DJEE%2BAdvanced&p%5B%5D=facets.exams%255B%255D%3DJEE%2BMAIN&p%5B%5D=facets.exams%255B%255D%3DJEE%2BMain&p%5B%5D=facets.exams%255B%255D%3DJEE%2BMain%2B%2526%2BAdvanced&p%5B%5D=facets.exams%255B%255D%3DJEE%2BMain%2Band%2BAdvanced&p%5B%5D=facets.exams%255B%255D%3DNEET&p%5B%5D=facets.exams%255B%255D%3DNEET%257C%257CAIIMS%257C%257CJIPMER%257C%257CMEDICAL%2BENTRANCE&p%5B%5D=facets.exams%255B%255D%3DOther%2BEngineering%2BExams&sid=bks%2Cenp%2Cuhu&start={{NUM}}&ref=aae9bab1-a866-4a9f-ba83-118b7858fe17&ajax=true',
'http://www.flipkart.com/lc/pr/pv1/spotList1/spot1/productList?sid=bks%2Cenp%2Cuhu%2C50s&filterNone=true&start={{NUM}}&ajax=true&_=1427910340713',
'http://www.flipkart.com/books/educational-and-professional/entrance-exams-preparation/engineering/pr?sid=bks%2Cenp%2Cuhu%2C50s&start={{NUM}}&ref=b33950b6-9a5b-4a2e-b02e-4298a470c7e0&ajax=true'
]

ini = "//div[@class='gd-col gu12 browse-product fk-inf-scroll-item']"
dictionary = {
	"img": "/div[@class='list-unit']/div[@class='gd-row']/div[@class='gd-col gu3 lu-image-wrapper']/div[@class='lu-image']/a[@class='lu-image-link ']/img/@src",
	"URL":"/div[@class='list-unit']/div[@class='gd-row']/div[@class='gd-col gu9']/div[@class='gd-row'][1]/div[@class='gd-col gu9']/div[@class='lu-title-wrapper']/a[@class='lu-title']/@href",
	"Votes":"/div[@class='list-unit']/div[@class='gd-row']/div[@class='gd-col gu9']/div[@class='gd-row'][1]/div[@class='gd-col gu9']/div[@class='lu-title-wrapper']/div[@class='pu-rating']/div[@class='rating-wrapper']/text()",
	"Author":"/div[@class='list-unit']/div[@class='gd-row']/div[@class='gd-col gu9']/div[@class='gd-row'][2]/div[@class='gd-col gu5']/div[@class='rpadding20 lu-info-wrapper']/div[@class='lu-description fk-font-11 tpadding5']/div[@class='author']/text()[2]",
	"Title":"/div[@class='list-unit']/div[@class='gd-row']/div[@class='gd-col gu9']/div[@class='gd-row'][1]/div[@class='gd-col gu9']/div[@class='lu-title-wrapper']/a[@class='lu-title']/text()",
	"price":"/div[@class='list-unit']/div[@class='gd-row']/div[@class='gd-col gu9']/div[@class='gd-row'][2]/div[@class='gd-col gu4']/div[@class='pu-price']/div[@class='pu-final fk-font-17 fk-bold']/text()"
	# "year":"//div[@class='year-released'][2]/text()[2]"
}
# key = "//a[@class='lu-title']/@href"
items = [20,90]
iterator = 1
f = open('urls.txt','w')
f.close()
for i in range(0,len(urls)) : 
	items = [20,90]
	ii = 1
	print '1: '
	while(len(items)*ii) > 0:
		# print '2: '
		url = urls[i].split('{{NUM}}')
		page = requests.get(url[0]+str(ii*20)+url[1])
		print url[0]+str(ii*20)+url[1]
		ii +=1
		# print '\n\n\n'+url[0]+str(ii*20)+url[1]+'\n\n\n'
		try:
			tree = etree.HTML(page.text)
		except: 
			ii=0

			# items =  tree.xpath(key)
		# f=open('urls.txt','a')
		items = tree.xpath(ini)
		# print '\n\n\n\n\n\n\n\n\n'+ str(len(items))+'\n-----\n\n'
		replace = ['\\xa0','\r','\n','\\t',"u'",'"',"\\n","\\r","'",'[',']','  ']
		temp = 1
		for item in range(0,len(items)):
			tempRow=[]
			# print '\n\n-----\n\n'
			for key in dictionary: 				
				xpath = ini + "["+str(item+1)+"]"+dictionary[key]
				out = str(tree.xpath(xpath))
				for rem in replace: 
					while rem in out: 
						out = out.replace(rem,'')
				tempRow.append(out)
			f = open('urls.txt','a')
			f.write("var.append([")
			for iii in tempRow: 
				f.write('"'+iii.strip()+'",')
			f.write('])\n')
			f.close()
				





			# print key+'\t\t: \t'+(((str(t)).replace('\n','')).replace('  ','')).replace(' ,',',')
		# print str(len(t)*iterator )0
		# iterator+=1
		# for j in items: 

		# 	f.write('http://www.flipkart.com'+j+'\n')
		# f.close()



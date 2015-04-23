import os 

current = os.getcwd()
os.chdir(current+r'\htmls-new')


fileList=  os.listdir(os.getcwd())

for i in fileList:
	if ".html" in i:  
		f = open(i,'r')
		text = f.read()
		f.close()
		text = text.replace('src="','src="file:///D:/scrappers/html2pdf/htmls-new/')

		f = open(i,'w')
		f.write(text)


import pdfkit,os,codecs,random



def html2pd(filename):
	

# 	print """
# 	---------------------------------------------------------

# """+filename+"""
# 	--------------------------------------------------------

# 	"""
	fileList = os.listdir(os.getcwd())
	cssList = []
	for i in fileList: 
		if '.css' in i: 
			cssList.append(i)
		else: 
			pass

	options = {
	    'page-size': 'A4',
	    'margin-top': '1.00in',
	    'margin-right': '0.75in',
	    'margin-bottom': '1.00in',
	    'margin-left': '0.75in',
	    'encoding': "UTF-8",
	    'no-outline': None,
	    'quiet': ''
	}
	config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
	for i in cssList: 
		pdfkit.from_file(filename,i.split('.')[0]+'-'+filename.replace('.html','') + '.pdf',configuration=config, options=options, css = i)
	# print 'done'

home = os.getcwd()
os.chdir(os.getcwd()+r'\htmls-new-allf')

extraHead = """
<html>
<head>
	<link rel="stylesheet" type="text/css" href="cms.css">
  <title></title>
</head>
<body>"""


extraTail = """
</body>
</html>
"""

allFiles = os.listdir(os.getcwd())

for i in allFiles: 
	if '.html' in i: 
		f= open(i, 'r')
		# print i
		body = f.read()
		# print body
		
		if '<link rel="stylesheet" type="text/css" href="cms.css">' not in body: 
			f.close()
			f=open(i,'w')
			f.write((extraHead+ body + extraTail))
		f.close()
		try:
			html2pd(i)
			print ("Success: "+i)
		except: 
		 	print ("Failed: "+i)
import pdfkit,os,codecs,random



def html2pd(filename):

	print """
	---------------------------------------------------------

"""+filename+"""
	--------------------------------------------------------

	"""

	options = {
	    'page-size': 'A4',
	    'margin-top': '0.75in',
	    'margin-right': '0.75in',
	    'margin-bottom': '0.75in',
	    'margin-left': '0.75in',
	    'encoding': "UTF-8",
	    'no-outline': None,
	    # 'quiet': ''
	}
	config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
	pdfkit.from_file(filename,str(random.randrange(90,892032)) + '.pdf',configuration=config, css = 'cms.css',options=options)
	print 'done'

os.chdir(os.getcwd()+r'\htmls')

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
		print i
		body = f.read()
		print body
		
		if '<link rel="stylesheet" type="text/css" href="cms.css">' not in body: 
			f.close()
			f=open(i,'w')
			f.write((extraHead+ body + extraTail))
		f.close()
		# try:
		html2pd(i)
		print ("Success: "+i)
		# except: 
		# 	print ("Failed: "+i)
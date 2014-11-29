import zipfile, re, os
records = []
for filename in os.listdir():
	try:
		docx = zipfile.ZipFile(filename)
		content = docx.read('word/document.xml')
		# print(str(content).count('<w:t>'))
		cleaned = re.sub('<(.|\n)*?>',' ',str(content))
		cleaned = re.sub("\'[a-z0-9]+",' ',str(cleaned))
		removals = ['\n','\\n','\t','\\t','\r','\\r','!',',','$','%','^','*','(',')','{','}','[',']','|','\\',':',';','>','.',',','?','/','_','`','~']
		for rem in removals:
		    cleaned = cleaned.replace(rem,' ')
		while '  ' in cleaned:
		    cleaned = cleaned.replace('  ',' ' )
		cleaned = cleaned.strip()
		print (cleaned)
		now =0 
		for i in range(0,len(cleaned)):
		    if cleaned[i] == ' ' or cleaned[i] == '\n' or cleaned[i] == '\\n':
		        now += 1

		print(now)
		records.append([filename,now])

	except:
		print('not a zip file')


for rec in records:
	print(rec)

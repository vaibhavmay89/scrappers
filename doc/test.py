import zipfile, re, os
records = []
cwd = os.getcwd()

records = []
def readdocfile(filename):
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
		# print (cleaned)
		now =0 
		for i in range(0,len(cleaned)):
		    if cleaned[i] == ' ' or cleaned[i] == '\n' or cleaned[i] == '\\n':
		        now += 1
		return(now)
	except:
		# print('not a zip file')
		return('NULL')

		
def clean(add):
	global cwd
	# print(cwd+add)
	rem = [str(cwd),'\\']
	for rems in rem:
		add = add.replace(rems,'/')
	add = add.replace('//','/')
	return(add)

def scavenger(add):
	global records, cwd

	for filename in os.listdir(add):
		if os.path.isfile(filename) == True:
			now = readdocfile(filename)
			records.append([str(clean(add)),filename,now])

		else:
			try:
				scavenger(str(add)+'\\'+filename)
			except:
				continue
				# print("cant identify: '"+ filename+"'")
			


scavenger(cwd)
f = open('stats.csv','w')
for rec in records:
	for val in rec:
		f.write(str(val))
		f.write(',')
	f.write('\n')
f.close()

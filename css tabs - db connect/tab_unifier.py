import os 


home=  os.getcwd()

# print os.listdir(home)

os.chdir(home+'\\resources')
current = os.getcwd()
templates = []
resources = os.listdir(current)
for i in resources:
	# print(i)
	f = open(i,'r').read()
	templates.append([i,f])
for i in templates:
	print i

os.chdir(home+'\\tabsdata')
current = os.getcwd()
folder = os.listdir(current)
print folder
for i in folder:
	tabNumName = []
	content = []
	os.chdir(current+'\\'+i)
	data = (os.listdir(os.getcwd()))
	print(data)
	for j in data:
		tabNumName.append([j.split(".")[0],j.split(".")[1]])
		f = open(j,'r').read()
		content.append([j,f])
	for l in tabNumName:
		print l



	new = ''
	new += templates[1][1]+ '\n'


	for j in range(0,len(data)):
		temp = templates[2][1].replace('{{anchor}}','tab'+str(tabNumName[j][0]))
		temp = temp.replace('{{tabName}}',tabNumName[j][1])
		templates[2][1] = templates[2][1].replace('id="current"','')
		new+= temp + '\n'
		temp = ''
		pass
	new += '</ul><div id="content" class="content1">'

	for jj in content: 
		print jj


	for j in range(0,len(data)):
		temp = templates[3][1].replace('{{anchor}}','tab'+str(tabNumName[j][0]))
		temp = temp.replace('{{content}}',content[j][1])
		new +=temp +'\n'
		temp = ''
		pass

	new  += templates[0][1]



print '------------------\n\n\n-------------------\n\n\n\n'

print new



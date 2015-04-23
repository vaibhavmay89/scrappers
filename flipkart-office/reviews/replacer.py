import os 
current = os.getcwd()

replace = ['\r','\n']
final = open('final.csv','w')
final.write('"')
os.chdir(current+ r'\reviews')
fileList = os.listdir(os.getcwd())
for i in fileList: 
	f = open(i,'r')
	text = f.read()
	f.close()
	for j in replace: 
		
			# print '.'
		text = text.replace(j,chr(10))
	final.write(text+'"\n"')



print chr(13)
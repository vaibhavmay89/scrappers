import re,os
os.chdir('C:/Users/vaibhav.singhal/secrets')

def checkseq(number):
	lis = []
	for i in number: 
		try:
			lis.append(int(i))
		except:
			print i
			return(1)
	# print lis
	ratio =0
	diff = [] 
	string = ''
	for  i in range(0,len(lis)-1):
		diff.append(lis[i]-lis[i+1])
	for i in range(0,len(diff)):

		if diff[i] < 0:
			diff[i] = -diff[i]
		string +=str(diff[i])
	seq = 0.0

	for i in string: 
		if i == '1':
			seq += 1.0/len(string)
		# print seq

	
	return(seq)
	return(j)



def similarity(number):
	lis = []
	for i in number: 
		lis.append(i)
	ratio =0

	for i in lis:
		temp = 0
		for j in lis:
			if i == j: 
				temp += 1.0/len(number)
				

		if temp> ratio:
			ratio = temp
			maxnum = i 
		else:
			pass 

	return(ratio) 
f = open('mobilefiltering.csv','r')
reject= []
data = f.readlines()
reRemoval = [r'[a-zA-Z]+']#,r]
for i in range(0,len(reRemoval)):
	reRemoval[i] = re.compile(reRemoval[i]) 
f = open('reject2.txt','w')
# data = data[0].split('\n')
removal = ['+91','-','\n','91+','91 ',' ','+undefined',"+",'"','n']

for i in range(0,len(data)):
	data[i] = data[i].replace('\n','')
	data[i] = data[i].split(',')
	for j in range(0,len(removal)):
		data[i][1] = data[i][1].replace(removal[j],'')
	for j in reRemoval:
		t = re.findall(j,data[i][1])
		if len(t)> 0 :
			reject.append(data[i])
			f.write(str(data[i])+"\t| Rejected By Regex\n")
			continue
			# print t
	if len(data[i][1])>13 or len(data[i][1])<10:
		# 
		reject.append(data[i])
		f.write(str(data[i])+"\t| Rejected By Length\n")
		continue
		# print data[i][1]
	if similarity(data[i][1])>0.5:
		reject.append(data[i])
		f.write(str(data[i])+"\t| Rejected due to Similarity\n")
		continue
		# print data[i][1]
	if checkseq(data[i][1])>0.7:
		reject.append(data[i])
		f.write(str(data[i])+"\t| Rejected due to Sequence\n")
		continue
		

# for row in data: 
# 	print row
# for i in data: 
# 	if i in reject:
# 		pass
# 	else:
# 		print i[1]
print len(data)
print len(reject)
rem = ['[',']',"'",'"']
f.close()
f=open('reject2.txt','r')
print(f.read())
f.close()

f = open('accepted.txt','w')
for i in data:
	if i in reject:
		pass
	else:
		temp = str(i)
		for j in rem:
			temp = temp.replace(j,'') 
		f.write(temp+"\n")
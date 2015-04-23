import os,random


current = os.getcwd()

files = os.listdir(current)

synonyms = []
template = []

for i in range(0,len(files)): 
	if ".syn" in files[i]:
		synonyms.append(files[i])
	elif '.tml' in files[i]: 
		template.append(files[i])
	elif '.list' in files[i]:
		topic = files[i] 

	else:
		pass

reviews = []
f = open(topic,'r')
topic = f.readlines()

for i in range(0,len(topic)): 
	topic[i]=topic[i].replace('\n','')

for i in template: 
	f = open(i)
	reviews = f.readlines()

for i in range(0,len(reviews)): 
	reviews[i]=reviews[i].replace('\n','')


# print synonyms
synList = []
for i in synonyms: 
	f = open(i,'r')
	temp = f.readlines()
	for i in range(0,len(temp)): 
		temp[i] = temp[i].replace('\n','')
	synList.append(temp)

dictionary = []
for i in range(0,len(synList)): 
	for j in synList[i]: 
		dictionary.append(j)
final = []
# for i in dictionary: 
# 	print i 
f = open('final.list','a')
f.write('\n')
for j in range(0,30):
	for i in reviews: 
		# print i 
		temp = []
		temp.append(i)
		for j in dictionary: 
			ini = i
			if ' '+j in i: 
				for k in synList: 
					if j in k:
						i=ini
						t = random.randrange(0,len(k)-1)
						# print '-->'+k[t]+'  <--> '+j
						i = i.replace(' '+j,' '+k[t])
						temp.append(i)
						# print '-->'+temp[1]
						
						# f.write(temp[1]+'\n')
						final.append(temp[1])
						temp.pop(1)

for i in reviews: 
	final.append(i)
# print final
random.shuffle(final)
for i in final:
	f.write(i+'\n')







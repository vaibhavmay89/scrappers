f = open('template.txt','r')
g = open('data.csv','r')
r = open('result.txt','w')
template = f.read()
csv = g.readlines()

data = []

for i in range(0,len(csv)): 
	data.append(csv[i].split(',')) 

header = data[0]

actualData = data[1:len(data)-1]

for i in range(0,len(actualData)): 
	temp = template
	for j in range(0,len(header)):
		temp =  temp.replace('{{'+header[j]+'}}',actualData[i][j])

	r.write('\n\n=======================================\n')
	r.write(temp)


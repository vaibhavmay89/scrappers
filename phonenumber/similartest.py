
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


def checkseq(number):
	lis = []
	for i in number: 
		lis.append(int(i))
	print lis
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

	print string

	return(seq)



print(checkseq('9560100123'))

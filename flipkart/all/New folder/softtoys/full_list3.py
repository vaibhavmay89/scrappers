#[]
full = []


def filterst(st,j):
	
	######### ALL ###########
	remove = ['[',']','"',"'"]
	#print(type(st))
	for r in remove:
		st = st.replace(r,"")

	#print (st)
	if ((j == 1) or (j==3)): 
		remove = ["Rs.",","," "]
		for r in remove:
			st = st.replace(r,'')
	if (j == 2): 
		remove = ["OFF",","," "]
		for r in remove:
			st = st.replace(r,'')

	


	return st


#[ 'name',  'cost',  "discount",  "originalPrice",  "ratings",  "noReviews",  "votes",  "speckey",  "specvalue",  'ImageURL' ]
specs = []
filter = 0 
for i in range (0,len(full)):
	for j in range(0,len(full[i][7])):
		if full[i][7][j] in specs:
			filter +=1
			continue
			
		else:

			specs.append(full[i][7][j])

for i in specs: 
	print (i)
print(str(len(specs)) +"    "+str(filter))


### NAME , Brand , PRICE , specs , 
###	for i in range(0,len(full[0])):
###	print(str(i)+":   "+str(full[0][i]))

new = []

for i in range (0,len(full)):
	new.append([full[i][0], full[i][1], full[i][2], full[i][3], full[i][4], full[i][5], full[i][6]])
	#for j in range(0,len(full[i][7])):
	for k in range(0,len(specs)) :
		try:
			#print("found one")
			index = full[i][7].index(specs[k])
			new[i].append(full[i][8][index])
			#print(str(i)+ ":   "+ full[i][8][index])
		except:
			new[i].append("N/A")


# building header
t = ''
for s in specs: 
	t += s+ '"|"'

f = open("final.csv","w")
f.write('"name"|"cost"|"discount"|"originalPrice"|"ratings"|"noReviews"|"votes"|"'+ t+'"|ImageURL"')


for i in range(0,len(new)):
	f.write("\n")
	for j in range(0,len(new[i])):
		#print(j)
		f.write(filterst(str(new[i][j]),j)+"|")
# for row in new: 
# 	f.write("\n"+ str(row))

f.close()





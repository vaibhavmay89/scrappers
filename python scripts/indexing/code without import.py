step = 10
import csv

print '---------- STEP 1/4: Data Import .. (starting) ------------------------'

data = []
with open('data.csv', 'r') as f:
   reader = csv.reader(f,delimiter = ',')
   for row in reader:
       data.append(row)


print '---------- STEP 1/4: IMPORTED SUCCESSFULLY ------------------------'
print '---------- STEP 2(a)/4 Indexing -------------------------------------'

allWords = []
index = []
index_summ = []
## [[['word'],[[doc,pos],[doc,pos]]],
##	[['word'],[[doc,pos],[doc,pos]]],
##  [['word'],[[doc,pos],[doc,pos]]]]
for i in range(0,len(data)):
    if i%step == 0:
        print 'Indexing .... (' + str(i*100.00/len(data)) +'% Finished)'
    temp =  data[i][0].split(' ')
    for j in range(0,len(temp)): 
        if temp[j] not in allWords: 
            allWords.append(temp[j])
            index.append([[temp[j]],[[i,j]]])
        else:
            for ii in range(0,len(allWords)):
                if(temp[j] == allWords[ii]):
                    index[ii][1].append([i,j])
file = open("Index.txt", "w")

print '---------- STEP 2(b)/4 Index Writing -------------------------------------'

for wi in range(0,len(index)):
    if wi%step == 0:
        print 'Writing Index .... (' + str(wi*100/len(data)) +'% Finished)'
    file.write(str(index[wi]))
    file.write('\n')
file.close()
print '---------- STEP 2:/4 Indexed Successfully-------------------------------------'
print '---------- STEP 3:/4 Summarising -------------------------------------'

for i in range(0,len(index)): 
    if i%step == 0:
        print 'Summarising .... (' + str(i*100/len(index)) +'% Finished)'
    nod =[]
    for j in range(0,len(index[i][1])):
        #print '1:' + str(index[i][1][j][0])
        if index[i][1][j][0] not in nod:
            #print '2:'
            nod.append(index[i][1][j][0])
    index_summ.append([index[i][0], len(index[i][1]),len(nod)])
print '---------- STEP 3/4 Summarized Successfully-------------------------------------'
print '---------- STEP 4/4 Finishing reports -------------------------------------'
file = open("index_summary.txt", "w")
for wwi in range(0,len(index_summ)):
    if wwi%step == 0:
        print 'Summarising .... (' + str(wwi*100/len(index)) +'% Finished)'
    file.write(str(index_summ[wwi]))
    file.write('\n')
file.close()
print '---------- STEP 4/4 Finished reports successfully-------------------------------------'
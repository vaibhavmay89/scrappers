replace = []


import os
def list2string(st,removal = 0,regexConv = 0):
	p = ''
	for i in st:
		p += i
	
	return(p)




current = os.getcwd()
new = os.chdir(current+'\\target-css')
target_list = os.listdir(current+'\target-css')
tfiles = []

for i in target_list:
	f = open(i,'r')
	c = f.readlines()
	f.close()
	c = list2string(c)
	tfiles.append(c)


for i in replace:
	for j in range(0,len(target_list)):
		rep = ('/* this has been auto-removed vide ref: enum='+ str(i[0])+'|targetcss='+target_list[j]+'*/')
		tfiles[j] = tfiles[j].replace(rep,'/* this has been recovered vide ref: enum='+ str(i[0])+'|targetcss='+target_list[j]+'*/'+i[3])
		f= open(target_list[j],'w')
		f.write(tfiles[j])
		f.close()


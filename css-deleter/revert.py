replace = []

replace.append(['1','1.css','1.css',"""h1 {
    font-family: 'Varela Round', sans-serif;
    background: 
    #d6d6d6;
    padding: 2px;}

"""])
replace.append(['2','1.css','1.css',"""h1 {
    font-family: 'Varela Round', sans-serif;
    background: 
    #d6d6d6;
    padding: 2px;}

"""])
replace.append(['3','1.css','1.css',"""h1 {font-family: 'Varela Round', sans-serif;background:#d6d6d6;padding: 2px;}


"""])
replace.append(['4','1.css','1.css',"""h1 {
    font-family: 'Varela Round', sans-serif;
    background: 
    #d6d6d6;
    padding: 2px
;}


"""])
replace.append(['5','1.css','1.css',"""h1 {
    font-family: 'Varela Round', sans-serif;
    background: 
    #d6d6d6 ;

    padding:  2px;}

"""])
replace.append(['6','1.css','1.css',"""h1 {
    font-family : 'Varela Round', sans-serif;
    background: 
    #d6d6d6;
    padding: 2px;}


"""])

import os
def list2string(st,removal = 0,regexConv = 0):
	p = ''
	for i in st:
		p += i
	
	return(p)




current = os.getcwd()
new = os.chdir(current+'\\target-css')
target_list = os.listdir()
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
		new = tfiles[j].replace(rep,'/* this has been recovered vide ref: enum='+ str(i[0])+'|targetcss='+target_list[j]+'*/'+i[3])
		f= open(target_list[j],'w')
		f.write(new)
		f.close()


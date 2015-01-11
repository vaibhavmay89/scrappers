import os 
import re

def list2string(st,removal = 0,regexConv = 0):
	p = ''
	for i in st:
		p += i
	rem = [' ','\n']
	if removal == 1:
		for i in rem: 
			p = p.replace(i,'')
	n = ''
	if regexConv ==1: 
		
		for i in p:
			n += i+'\\n*\\s*'
			
		# n = n.replace('\\s','\s')
		regexsplchars = ['(','{','[','-','.','?',']','}',')']
		# print(len(n))
		for spl in regexsplchars:
			# print("we are in :" + spl +'\t\t'+ ("\\"+spl) )
			# print(n)
			n = n.replace(spl,("\\"+spl))
		# print(len(n))
		return(n)

	return(p)


current = os.getcwd()

# Acquiring  Source Files 

new = os.chdir(current+'\\source-css')
source_list = os.listdir()
sfiles = []

for i in source_list:
	f = open(i,'r')
	c = f.readlines()
	f.close()
	sfiles.append(list2string(st=c,removal=1,regexConv=1))

# Acquiring Target Files 

new = os.chdir(current+'\\target-css')
target_list = os.listdir()
tfiles = []

for i in target_list:
	f = open(i,'r')
	c = f.readlines()
	f.close()
	c = list2string(c)
	tfiles.append(c)

log = []
enum = 1

for s in range(0,len(sfiles)): 
	for t in range(0,len(tfiles)):
		# print(sfiles[s])

		regObj = re.compile(sfiles[s],re.I)
		# re.DEBUG
		match = re.findall(sfiles[s],tfiles[t])
		if match != None:
			text= match
			for instance in match:
				log.append([enum,source_list[s],target_list[t],instance])
				f = open(target_list[t],'w')
				# print(f)
				tfiles[t] = tfiles[t].replace(instance,('\n/* this has been auto-removed vide ref: enum='+ str(enum)+'|targetcss='+target_list[t]+'*/\n'),1)
				print("-------------------------------"+target_list[t]+"===================================")
				f.write(tfiles[t])
				f.close()


				print('/* this has been auto-removed vide ref: enum='+ str(enum)+'|targetcss='+target_list[t]+'*/')
				enum +=1
		else:
			print("NONE FOUND")
# OUTPUTTING revert.py 
os.chdir(current)
f = open('revert.py','w')
f.write("replace = []\n\n")
for i in log: 
	f.write("replace.append(['"+str(i[0])+"','"+i[1]+"','"+i[2]+"',"+'"""'+i[3]+'"""'+"])\n")

f.write("""
import os
def list2string(st,removal = 0,regexConv = 0):
	p = ''
	for i in st:
		p += i
	
	return(p)




current = os.getcwd()
new = os.chdir(current+'\\\\target-css')
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

"""
)

# for i in log: 







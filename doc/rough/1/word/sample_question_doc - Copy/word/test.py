from xml.dom import minidom

xmldoc = minidom.parse('document.xml')
now = 0
for a in xmldoc.getElementsByTagName('w:t'): 
	p = str(a.firstChild.data)
	print(p)
	for i in p: 
		if i == ' ':
			now += 1 
		else:
			continue
	now += 1
print(now)
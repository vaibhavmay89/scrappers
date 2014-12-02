from xml.dom import minidom

xmldoc = minidom.parse('document.xml')

for a in xmldoc.getElementsByTagName('w:t'): 
	print(a.firstChild.data)
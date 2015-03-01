import os 
from PIL import Image, ImageFilter

print os.listdir(os.getcwd())
# 3d_abstract_white-1920x1080.jpg
im = Image.open('2014827-1451382-1012-Capture.PNG')
s = im.size
ts = [345,675]
size = (1,40)
compression = [345.0/s[0],675.0/s[1]]
if compression[0]< compression[1]: 
	size = (1000000,size[1])
else:
	size = (size[0],1000000)
print size
deg = 45
im.rotate(deg)
im = im.convert('RGB')
im.thumbnail(size,Image.ANTIALIAS)
home = os.getcwd()
splittedpath = os.path.split('G:\\scrapper\\scrappers\\CMS Optimized Images compression\\Optimized Images\\cdn1\\Optimized Images\\2014827-1451382-1012-Capture.jpg')
os.chdir(splittedpath[0])
im.save(splittedpath[1], "JPEG",quality=50, optimize=True, progressive=True)
os.chdir(home)

print('==============================')

x = 9
x = x*1.0
print x

print('==============================')
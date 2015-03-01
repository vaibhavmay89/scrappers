import os 
from PIL import Image, ImageFilter

print os.listdir(os.getcwd())
# 3d_abstract_white-1920x1080.jpg
im = Image.open('3d_abstract_white-1920x1080.jpg')
# print f.show()

size = 128, 128

im.thumbnail(size)
im.save('sdsd.jpg', "JPEG")
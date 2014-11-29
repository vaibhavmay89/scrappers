import zipfile
import os
import shutil

print (os.listdir())
docxfiles = []
for filename in os.listdir():
    if ".docx" in filename:
       docxfiles.append(filename)
        
for k in docxfiles:
    shutil.copy( k, os.getcwd()+'/rough/'+k)

os.chdir((str(os.getcwd())+'\\rough'))
print (os.listdir())
for filename in os.listdir():
    if ".docx" in filename:
       os.rename(filename,filename.replace('.docx','.zip'))

print (os.listdir())



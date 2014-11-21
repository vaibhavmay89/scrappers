import os 
import  shutil

new_path = "C:/Users/vaibhav.singhal/Desktop/python scripts/batch studeny/new"
src = "C:/Users/vaibhav.singhal/Desktop/python scripts/batch studeny/"
q =  os.listdir("C:/Users/vaibhav.singhal/Desktop/python scripts/batch studeny/")


files = ["Mohammed Anas khan.jpg","Shabaaz Basheer.jpg","Allen john Alex.jpg","Ashwin Satheesh_Arya 6.JPG","Sanyukta Kalikar.jpg","Venkata Dhiren Seera.JPG","Neha Shibu Elenjickal.jpg","Homi A25","Rama 2_Roshan Mujeeb.JPG","Arkaprabha.jpg","sitoshna.jpg","Juhi Josh.jpg","Nayonika Bhattacharya.jpg","Kelvin De Costa_Homi A24.jpg","Nina Ann Stephen.jpg","Homi A22_AHANGJEET.jpg","Atreya Majumdar.JPG","Mathangi Krishnan.jpg","A13R2110160_M.Sudarsan Balaji_HomiA21.jpg"]

#os.path.join(src, files[i])
for i in range(0,len(files)):
	try:
		shutil.copy2(os.path.join(src, files[i]), os.path.join(new_path, files[i]))
	except: 
		print "error in copying "+ files[i]

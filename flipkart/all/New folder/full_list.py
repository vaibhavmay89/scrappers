#[]
full = []

full.append([['Sennheiser CX 180 Street II In-ear-canalphone'], [' Rs. 841 '], ['15% OFF'], [' Rs. 990 '], ['4.3'], ['869'], ['2021'], ['Headset Design', 'Brand', 'Wired/Wireless', 'Controls', 'Headphone Type', 'Model ID', 'Other Performance Features', 'Sensitivity', 'Impedance', 'Frequency Response', 'Weight', 'Warranty Summary', 'Cord Type'], ['In-ear-canalphone', 'Sennheiser', 'Wired', 'Innovative Finger-Contoured', 'In-the-ear', 'CX 180', 'Bass-driven Stereo Sound, High Passive Attenuation of Ambient Noise, Active Noise Cancellation', '110 dB/mW (Power On)', '16 ohm (Power On)', '20 - 20000 Hz', '5 g', '2 Years Warranty', '1.2 m Symmetric Cord'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Philips SHE1360/97 Wired Headphones'], [' Rs. 111 '], [], [], ['4.2'], ['1,137'], ['3281'], ['Headset Design', 'Brand', 'Wired/Wireless', 'Headphone Type', 'Model ID', 'Color', 'Maximum Power Input', 'Other Performance Features', 'Sensitivity', 'Impedance', 'Headphone Driver Units', 'Frequency Response', 'Warranty Summary', 'Headphone Jack'], ['In the Ear', 'Philips', 'Wired', 'Earbud', 'SHE1360/97', 'Black', '50 mW', 'Bass Beat Vents for Better Sound', '100 dB/mW (Power On)', '16 ohm (Power On)', '15 mm', '16 - 20000 Hz', '6 Months Warranty', '3.5 mm'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Sennheiser HD 180'], [' Rs. 841 '], ['15% OFF'], [' Rs. 990 '], ['4'], ['447'], ['1227'], ['Frequency Response', 'Headset Design', 'Brand', 'Wired/Wireless', 'Compatible Devices', 'Headphone Type', 'Model ID', 'Color', 'Warranty Summary', 'Weight'], ['21 - 18000 Hz', 'Over the Ear', 'Sennheiser', 'Wired', 'Laptops, PC, Computer, Mobile', 'Over the Head (Circumaural), Closed Back', 'HD 180', 'Black', '2 Years Warranty Sennheiser India Warranty and Free Transit Insurance', '130 g'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Creative EP-600 Headphone'], [' Rs. 339 '], ['32% OFF'], [' Rs. 499 '], ['3.6'], ['300'], ['907'], ['Headset Design', 'Brand', 'Wired/Wireless', 'Headphone Type', 'Model ID', 'Magnet Type', 'Other Performance Features', 'Sensitivity', 'Impedance', 'Headphone Driver Units', 'Frequency Response', 'Weight', 'Warranty Summary', 'Cord Type', 'Additional Features'], ['In the Ear', 'Creative', 'Wired', 'Canalphone', 'EP-600', 'Neodymium', 'Noise Isolation', '100 dB/mW (Power On)', '16 ohm (Power On)', '10 mm', '20 - 20000 Hz', '12 g', '6 Months of Manufacturer Warranty.', '1.2 m', 'Ergonomic Design, Soft Silicone Ear Bud'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Philips SBCHL140/98 Wired Headphones'], [' Rs. 239 '], ['20% OFF'], [' Rs. 299 '], ['3.7'], ['73'], ['285'], ['Other Performance Features', 'Maximum Power Input', 'Sensitivity', 'Impedance', 'Headphone Driver Units', 'Frequency Response', 'Headset Design', 'Brand', 'Wired/Wireless', 'Headphone Type', 'Model ID', 'Magnet Type', 'Color', 'Warranty Summary', 'Headphone Jack', 'Connector Plating', 'Cord Type', 'Additional Features'], ['Air Vents for Rich Deep Sound', '100 mW', '96 dB/mW (Power On)', '32 ohm (Power On)', '30 mm', '18 - 20000 Hz', 'On the Ear', 'Philips', 'Wired', 'Over the Head (Supra-aural), Closed Back', 'SBCHL140/98', 'Ferrite', 'Graphite', '6 Months Warranty', '3.5 mm', 'Chrome Plated', '1 m Two-Parallel Symmetric- Copper Cord', 'Ultra Lightweight , Reinforced Cable Connection'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Creative EP-630 earphone In-the-ear Headphone'], [' Rs. 575 '], ['42% OFF'], [' Rs. 999 '], ['4.4'], ['775'], ['2311'], ['Headset Design', 'Brand', 'Headphone Type', 'Model ID', 'Warranty Summary'], ['Ear Bud', 'Creative', 'Earbud', 'CR EP-630', '6 months Creative India warranty.'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['JBL J03B Tempo Wired Headphones'], [' Rs. 3,000 '], ['11% OFF'], [' Rs. 3,400 '], ['4.4'], ['980'], ['2620'], ['Other Performance Features', 'Headphone Driver Units', 'Frequency Response', 'Headset Design', 'Brand', 'Wired/Wireless', 'Compatible Devices', 'Headphone Type', 'Model ID', 'Color', 'Warranty Summary', 'Warranty Service Type', 'Power Supply', 'Headphone Jack', 'Connector Plating', 'Cord Type', 'Additional Features'], ['Powerful Clear JBL Sound', '40 mm', '20 - 20000 Hz', 'On the Ear', 'JBL', 'Wired', 'PC, Laptops, MP3 Player, CD Player, iPhones, iPod, iPad, Tablet', 'Over the Head (Supra-aural), Closed Back', 'J03B Tempo', 'Black', '1 Year Domestic Carry In Limited Warranty', 'Carry In', 'Audio Out Plug', '3.5 mm', 'Gold Plated', '1.2 m', 'Adjustable Padded Headband, Self Adjusting Earcup Alignment, Fold Flat Earcups'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])

#[ 'name',  'cost',  "discount",  "originalPrice",  "ratings",  "noReviews",  "votes",  "speckey",  "specvalue",  'ImageURL' ]

specs = []
filter = 0 
for i in range (0,len(full)):
	for j in range(0,len(full[i][7])):
		if full[i][7][j] in specs:
			filter +=1
			continue
			
		else:

			specs.append(full[i][7][j])

for i in specs: 
	print (i)
print(str(len(specs)) +"    "+str(filter))


### NAME , Brand , PRICE , specs , 
###	for i in range(0,len(full[0])):
###	print(str(i)+":   "+str(full[0][i]))

new = []

for i in range (0,len(full)):
	new.append([full[i][0], full[i][1], full[i][2], full[i][3], full[i][4], full[i][5], full[i][6]])
	for j in range(0,len(full[i][7])):
		for k in range(0,len(specs)) :
			try:
				#print("found one")
				index = full[i][7].index(specs[k])
				new[i].append(full[i][8][index])
				#print(str(i)+ ":   "+ full[i][8][index])
			except:
				new[i].append("N/A")


# building header
t = ''
for s in specs: 
	t += s+ "|"

f = open("final.txt","a")
f.write('"name"|"cost"|"discount"|"originalPrice"|"ratings"|"noReviews"|"votes"|"speckey"|"specvalue"|"ImageURL"')


for i in range(0,len(new)):
	f.write("\n")
	for j in new[i]:
		#print(j)
		f.write(str(j)+"|")
# for row in new: 
# 	f.write("\n"+ str(row))



#[]
full = []

full.append([['Sennheiser CX 180 Street II In-ear-canalphone'], [' Rs. 841 '], ['15% OFF'], [' Rs. 990 '], ['4.3'], ['869'], ['2021'], ['Headset Design', 'Brand', 'Wired/Wireless', 'Controls', 'Headphone Type', 'Model ID', 'Other Performance Features', 'Sensitivity', 'Impedance', 'Frequency Response', 'Weight', 'Warranty Summary', 'Cord Type'], ['In-ear-canalphone', 'Sennheiser', 'Wired', 'Innovative Finger-Contoured', 'In-the-ear', 'CX 180', 'Bass-driven Stereo Sound, High Passive Attenuation of Ambient Noise, Active Noise Cancellation', '110 dB/mW (Power On)', '16 ohm (Power On)', '20 - 20000 Hz', '5 g', '2 Years Warranty', '1.2 m Symmetric Cord'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Philips SHE1360/97 Wired Headphones'], [' Rs. 111 '], [], [], ['4.2'], ['1,137'], ['3281'], ['Headset Design', 'Brand', 'Wired/Wireless', 'Headphone Type', 'Model ID', 'Color', 'Maximum Power Input', 'Other Performance Features', 'Sensitivity', 'Impedance', 'Headphone Driver Units', 'Frequency Response', 'Warranty Summary', 'Headphone Jack'], ['In the Ear', 'Philips', 'Wired', 'Earbud', 'SHE1360/97', 'Black', '50 mW', 'Bass Beat Vents for Better Sound', '100 dB/mW (Power On)', '16 ohm (Power On)', '15 mm', '16 - 20000 Hz', '6 Months Warranty', '3.5 mm'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Sennheiser HD 180'], [' Rs. 841 '], ['15% OFF'], [' Rs. 990 '], ['4'], ['447'], ['1227'], ['Frequency Response', 'Headset Design', 'Brand', 'Wired/Wireless', 'Compatible Devices', 'Headphone Type', 'Model ID', 'Color', 'Warranty Summary', 'Weight'], ['21 - 18000 Hz', 'Over the Ear', 'Sennheiser', 'Wired', 'Laptops, PC, Computer, Mobile', 'Over the Head (Circumaural), Closed Back', 'HD 180', 'Black', '2 Years Warranty Sennheiser India Warranty and Free Transit Insurance', '130 g'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Creative EP-600 Headphone'], [' Rs. 339 '], ['32% OFF'], [' Rs. 499 '], ['3.6'], ['300'], ['907'], ['Headset Design', 'Brand', 'Wired/Wireless', 'Headphone Type', 'Model ID', 'Magnet Type', 'Other Performance Features', 'Sensitivity', 'Impedance', 'Headphone Driver Units', 'Frequency Response', 'Weight', 'Warranty Summary', 'Cord Type', 'Additional Features'], ['In the Ear', 'Creative', 'Wired', 'Canalphone', 'EP-600', 'Neodymium', 'Noise Isolation', '100 dB/mW (Power On)', '16 ohm (Power On)', '10 mm', '20 - 20000 Hz', '12 g', '6 Months of Manufacturer Warranty.', '1.2 m', 'Ergonomic Design, Soft Silicone Ear Bud'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Philips SBCHL140/98 Wired Headphones'], [' Rs. 239 '], ['20% OFF'], [' Rs. 299 '], ['3.7'], ['73'], ['285'], ['Other Performance Features', 'Maximum Power Input', 'Sensitivity', 'Impedance', 'Headphone Driver Units', 'Frequency Response', 'Headset Design', 'Brand', 'Wired/Wireless', 'Headphone Type', 'Model ID', 'Magnet Type', 'Color', 'Warranty Summary', 'Headphone Jack', 'Connector Plating', 'Cord Type', 'Additional Features'], ['Air Vents for Rich Deep Sound', '100 mW', '96 dB/mW (Power On)', '32 ohm (Power On)', '30 mm', '18 - 20000 Hz', 'On the Ear', 'Philips', 'Wired', 'Over the Head (Supra-aural), Closed Back', 'SBCHL140/98', 'Ferrite', 'Graphite', '6 Months Warranty', '3.5 mm', 'Chrome Plated', '1 m Two-Parallel Symmetric- Copper Cord', 'Ultra Lightweight , Reinforced Cable Connection'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Creative EP-630 earphone In-the-ear Headphone'], [' Rs. 575 '], ['42% OFF'], [' Rs. 999 '], ['4.4'], ['775'], ['2311'], ['Headset Design', 'Brand', 'Headphone Type', 'Model ID', 'Warranty Summary'], ['Ear Bud', 'Creative', 'Earbud', 'CR EP-630', '6 months Creative India warranty.'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['JBL J03B Tempo Wired Headphones'], [' Rs. 3,000 '], ['11% OFF'], [' Rs. 3,400 '], ['4.4'], ['980'], ['2620'], ['Other Performance Features', 'Headphone Driver Units', 'Frequency Response', 'Headset Design', 'Brand', 'Wired/Wireless', 'Compatible Devices', 'Headphone Type', 'Model ID', 'Color', 'Warranty Summary', 'Warranty Service Type', 'Power Supply', 'Headphone Jack', 'Connector Plating', 'Cord Type', 'Additional Features'], ['Powerful Clear JBL Sound', '40 mm', '20 - 20000 Hz', 'On the Ear', 'JBL', 'Wired', 'PC, Laptops, MP3 Player, CD Player, iPhones, iPod, iPad, Tablet', 'Over the Head (Supra-aural), Closed Back', 'J03B Tempo', 'Black', '1 Year Domestic Carry In Limited Warranty', 'Carry In', 'Audio Out Plug', '3.5 mm', 'Gold Plated', '1.2 m', 'Adjustable Padded Headband, Self Adjusting Earcup Alignment, Fold Flat Earcups'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])

#[ 'name',  'cost',  "discount",  "originalPrice",  "ratings",  "noReviews",  "votes",  "speckey",  "specvalue",  'ImageURL' ]

specs = []
filter = 0 
for i in range (0,len(full)):
	for j in range(0,len(full[i][7])):
		if full[i][7][j] in specs:
			filter +=1
			continue
			
		else:

			specs.append(full[i][7][j])

for i in specs: 
	print (i)
print(str(len(specs)) +"    "+str(filter))


### NAME , Brand , PRICE , specs , 
###	for i in range(0,len(full[0])):
###	print(str(i)+":   "+str(full[0][i]))

new = []

for i in range (0,len(full)):
	new.append([full[i][0], full[i][1], full[i][2], full[i][3], full[i][4], full[i][5], full[i][6]])
	for j in range(0,len(full[i][7])):
		for k in range(0,len(specs)) :
			try:
				#print("found one")
				index = full[i][7].index(specs[k])
				new[i].append(full[i][8][index])
				#print(str(i)+ ":   "+ full[i][8][index])
			except:
				new[i].append("N/A")


# building header
t = ''
for s in specs: 
	t += s+ "|"

f = open("final.txt","a")
f.write('"name"|"cost"|"discount"|"originalPrice"|"ratings"|"noReviews"|"votes"|"speckey"|"specvalue"|"ImageURL"')


for i in range(0,len(new)):
	f.write("\n")
	for j in new[i]:
		#print(j)
		f.write(str(j)+"|")
# for row in new: 
# 	f.write("\n"+ str(row))



#[]
full = []

full.append([['Sennheiser CX 180 Street II In-ear-canalphone'], [' Rs. 841 '], ['15% OFF'], [' Rs. 990 '], ['4.3'], ['869'], ['2021'], ['Headset Design', 'Brand', 'Wired/Wireless', 'Controls', 'Headphone Type', 'Model ID', 'Other Performance Features', 'Sensitivity', 'Impedance', 'Frequency Response', 'Weight', 'Warranty Summary', 'Cord Type'], ['In-ear-canalphone', 'Sennheiser', 'Wired', 'Innovative Finger-Contoured', 'In-the-ear', 'CX 180', 'Bass-driven Stereo Sound, High Passive Attenuation of Ambient Noise, Active Noise Cancellation', '110 dB/mW (Power On)', '16 ohm (Power On)', '20 - 20000 Hz', '5 g', '2 Years Warranty', '1.2 m Symmetric Cord'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Philips SHE1360/97 Wired Headphones'], [' Rs. 111 '], [], [], ['4.2'], ['1,137'], ['3281'], ['Headset Design', 'Brand', 'Wired/Wireless', 'Headphone Type', 'Model ID', 'Color', 'Maximum Power Input', 'Other Performance Features', 'Sensitivity', 'Impedance', 'Headphone Driver Units', 'Frequency Response', 'Warranty Summary', 'Headphone Jack'], ['In the Ear', 'Philips', 'Wired', 'Earbud', 'SHE1360/97', 'Black', '50 mW', 'Bass Beat Vents for Better Sound', '100 dB/mW (Power On)', '16 ohm (Power On)', '15 mm', '16 - 20000 Hz', '6 Months Warranty', '3.5 mm'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Sennheiser HD 180'], [' Rs. 841 '], ['15% OFF'], [' Rs. 990 '], ['4'], ['447'], ['1227'], ['Frequency Response', 'Headset Design', 'Brand', 'Wired/Wireless', 'Compatible Devices', 'Headphone Type', 'Model ID', 'Color', 'Warranty Summary', 'Weight'], ['21 - 18000 Hz', 'Over the Ear', 'Sennheiser', 'Wired', 'Laptops, PC, Computer, Mobile', 'Over the Head (Circumaural), Closed Back', 'HD 180', 'Black', '2 Years Warranty Sennheiser India Warranty and Free Transit Insurance', '130 g'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Creative EP-600 Headphone'], [' Rs. 339 '], ['32% OFF'], [' Rs. 499 '], ['3.6'], ['300'], ['907'], ['Headset Design', 'Brand', 'Wired/Wireless', 'Headphone Type', 'Model ID', 'Magnet Type', 'Other Performance Features', 'Sensitivity', 'Impedance', 'Headphone Driver Units', 'Frequency Response', 'Weight', 'Warranty Summary', 'Cord Type', 'Additional Features'], ['In the Ear', 'Creative', 'Wired', 'Canalphone', 'EP-600', 'Neodymium', 'Noise Isolation', '100 dB/mW (Power On)', '16 ohm (Power On)', '10 mm', '20 - 20000 Hz', '12 g', '6 Months of Manufacturer Warranty.', '1.2 m', 'Ergonomic Design, Soft Silicone Ear Bud'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Philips SBCHL140/98 Wired Headphones'], [' Rs. 239 '], ['20% OFF'], [' Rs. 299 '], ['3.7'], ['73'], ['285'], ['Other Performance Features', 'Maximum Power Input', 'Sensitivity', 'Impedance', 'Headphone Driver Units', 'Frequency Response', 'Headset Design', 'Brand', 'Wired/Wireless', 'Headphone Type', 'Model ID', 'Magnet Type', 'Color', 'Warranty Summary', 'Headphone Jack', 'Connector Plating', 'Cord Type', 'Additional Features'], ['Air Vents for Rich Deep Sound', '100 mW', '96 dB/mW (Power On)', '32 ohm (Power On)', '30 mm', '18 - 20000 Hz', 'On the Ear', 'Philips', 'Wired', 'Over the Head (Supra-aural), Closed Back', 'SBCHL140/98', 'Ferrite', 'Graphite', '6 Months Warranty', '3.5 mm', 'Chrome Plated', '1 m Two-Parallel Symmetric- Copper Cord', 'Ultra Lightweight , Reinforced Cable Connection'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Creative EP-630 earphone In-the-ear Headphone'], [' Rs. 575 '], ['42% OFF'], [' Rs. 999 '], ['4.4'], ['775'], ['2311'], ['Headset Design', 'Brand', 'Headphone Type', 'Model ID', 'Warranty Summary'], ['Ear Bud', 'Creative', 'Earbud', 'CR EP-630', '6 months Creative India warranty.'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['JBL J03B Tempo Wired Headphones'], [' Rs. 3,000 '], ['11% OFF'], [' Rs. 3,400 '], ['4.4'], ['980'], ['2620'], ['Other Performance Features', 'Headphone Driver Units', 'Frequency Response', 'Headset Design', 'Brand', 'Wired/Wireless', 'Compatible Devices', 'Headphone Type', 'Model ID', 'Color', 'Warranty Summary', 'Warranty Service Type', 'Power Supply', 'Headphone Jack', 'Connector Plating', 'Cord Type', 'Additional Features'], ['Powerful Clear JBL Sound', '40 mm', '20 - 20000 Hz', 'On the Ear', 'JBL', 'Wired', 'PC, Laptops, MP3 Player, CD Player, iPhones, iPod, iPad, Tablet', 'Over the Head (Supra-aural), Closed Back', 'J03B Tempo', 'Black', '1 Year Domestic Carry In Limited Warranty', 'Carry In', 'Audio Out Plug', '3.5 mm', 'Gold Plated', '1.2 m', 'Adjustable Padded Headband, Self Adjusting Earcup Alignment, Fold Flat Earcups'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])

#[ 'name',  'cost',  "discount",  "originalPrice",  "ratings",  "noReviews",  "votes",  "speckey",  "specvalue",  'ImageURL' ]

specs = []
filter = 0 
for i in range (0,len(full)):
	for j in range(0,len(full[i][7])):
		if full[i][7][j] in specs:
			filter +=1
			continue
			
		else:

			specs.append(full[i][7][j])

for i in specs: 
	print (i)
print(str(len(specs)) +"    "+str(filter))


### NAME , Brand , PRICE , specs , 
###	for i in range(0,len(full[0])):
###	print(str(i)+":   "+str(full[0][i]))

new = []

for i in range (0,len(full)):
	new.append([full[i][0], full[i][1], full[i][2], full[i][3], full[i][4], full[i][5], full[i][6]])
	for j in range(0,len(full[i][7])):
		for k in range(0,len(specs)) :
			try:
				#print("found one")
				index = full[i][7].index(specs[k])
				new[i].append(full[i][8][index])
				#print(str(i)+ ":   "+ full[i][8][index])
			except:
				new[i].append("N/A")


# building header
t = ''
for s in specs: 
	t += s+ "|"

f = open("final.txt","a")
f.write('"name"|"cost"|"discount"|"originalPrice"|"ratings"|"noReviews"|"votes"|"speckey"|"specvalue"|"ImageURL"')


for i in range(0,len(new)):
	f.write("\n")
	for j in new[i]:
		#print(j)
		f.write(str(j)+"|")
# for row in new: 
# 	f.write("\n"+ str(row))




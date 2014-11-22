#[]
<<<<<<< HEAD

def filterst(st,j):
	
	######### ALL ###########
	remove = ['[',']','"',"'"]
	#print(type(st))
	for r in remove:
		st = st.replace(r,"")

	#print (st)
	if ((j == 1) or (j==3)): 
		remove = ["Rs.",","," "]
		for r in remove:
			st = st.replace(r,'')
	if (j == 2): 
		remove = ["OFF",","," "]
		for r in remove:
			st = st.replace(r,'')

	


	return st



full = []

full.append([['Sennheiser CX 180 Street II In-ear-canalphone'], [' Rs. 841 '], ['15% OFF'], [' Rs. 990 '], ['4.3'], ['959'], ['2076'], ['Headset Design', 'Brand', 'Wired/Wireless', 'Controls', 'Headphone Type', 'Model ID', 'Other Performance Features', 'Sensitivity', 'Impedance', 'Frequency Response', 'Weight', 'Warranty Summary', 'Cord Type'], ['In-ear-canalphone', 'Sennheiser', 'Wired', 'Innovative Finger-Contoured', 'In-the-ear', 'CX 180', 'Bass-driven Stereo Sound, High Passive Attenuation of Ambient Noise, Active Noise Cancellation', '110 dB/mW (Power On)', '16 ohm (Power On)', '20 - 20000 Hz', '5 g', '2 Years Warranty', '1.2 m Symmetric Cord'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Philips SHE1360/97 Wired Headphones'], [' Rs. 111 '], [], [], ['4.2'], ['1,170'], ['3305'], ['Other Performance Features', 'Maximum Power Input', 'Sensitivity', 'Impedance', 'Headphone Driver Units', 'Frequency Response', 'Headset Design', 'Brand', 'Wired/Wireless', 'Headphone Type', 'Model ID', 'Color', 'Warranty Summary', 'Headphone Jack'], ['Bass Beat Vents for Better Sound', '50 mW', '100 dB/mW (Power On)', '16 ohm (Power On)', '15 mm', '16 - 20000 Hz', 'In the Ear', 'Philips', 'Wired', 'Earbud', 'SHE1360/97', 'Black', '6 Months Warranty', '3.5 mm'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Sennheiser HD 180'], [' Rs. 841 '], ['15% OFF'], [' Rs. 990 '], ['4'], ['481'], ['1240'], ['Frequency Response', 'Headset Design', 'Brand', 'Wired/Wireless', 'Compatible Devices', 'Headphone Type', 'Model ID', 'Color', 'Warranty Summary', 'Weight'], ['21 - 18000 Hz', 'Over the Ear', 'Sennheiser', 'Wired', 'Laptops, PC, Computer, Mobile', 'Over the Head (Circumaural), Closed Back', 'HD 180', 'Black', '2 Years Warranty Sennheiser India Warranty and Free Transit Insurance', '130 g'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Creative EP-600 Headphone'], [' Rs. 339 '], ['32% OFF'], [' Rs. 499 '], ['3.6'], ['329'], ['912'], ['Other Performance Features', 'Sensitivity', 'Impedance', 'Headphone Driver Units', 'Frequency Response', 'Headset Design', 'Brand', 'Wired/Wireless', 'Headphone Type', 'Model ID', 'Magnet Type', 'Warranty Summary', 'Weight', 'Cord Type', 'Additional Features'], ['Noise Isolation', '100 dB/mW (Power On)', '16 ohm (Power On)', '10 mm', '20 - 20000 Hz', 'In the Ear', 'Creative', 'Wired', 'Canalphone', 'EP-600', 'Neodymium', '6 Months of Manufacturer Warranty.', '12 g', '1.2 m', 'Ergonomic Design, Soft Silicone Ear Bud'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Philips SBCHL140/98 Wired Headphones'], [' Rs. 239 '], ['20% OFF'], [' Rs. 299 '], ['3.7'], ['76'], ['287'], ['Other Performance Features', 'Maximum Power Input', 'Sensitivity', 'Impedance', 'Headphone Driver Units', 'Frequency Response', 'Headset Design', 'Brand', 'Wired/Wireless', 'Headphone Type', 'Model ID', 'Magnet Type', 'Color', 'Warranty Summary', 'Headphone Jack', 'Connector Plating', 'Cord Type', 'Additional Features'], ['Air Vents for Rich Deep Sound', '100 mW', '96 dB/mW (Power On)', '32 ohm (Power On)', '30 mm', '18 - 20000 Hz', 'On the Ear', 'Philips', 'Wired', 'Over the Head (Supra-aural), Closed Back', 'SBCHL140/98', 'Ferrite', 'Graphite', '6 Months Warranty', '3.5 mm', 'Chrome Plated', '1 m Two-Parallel Symmetric- Copper Cord', 'Ultra Lightweight , Reinforced Cable Connection'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Creative EP-630 earphone In-the-ear Headphone'], [' Rs. 574 '], ['42% OFF'], [' Rs. 999 '], ['4.4'], ['820'], ['2366'], ['Headset Design', 'Brand', 'Headphone Type', 'Model ID', 'Color', 'Warranty Summary'], ['Ear Bud', 'Creative', 'Earbud', 'EP-630', 'Black', '6 months Creative India warranty.'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['JBL J03B Tempo Wired Headphones'], [' Rs. 1,999 '], [], [], ['4.4'], ['1,013'], ['2624'], ['Headset Design', 'Brand', 'Wired/Wireless', 'Compatible Devices', 'Headphone Type', 'Model ID', 'Color', 'Other Performance Features', 'Headphone Driver Units', 'Frequency Response', 'Warranty Summary', 'Warranty Service Type', 'Power Supply', 'Headphone Jack', 'Connector Plating', 'Cord Type', 'Additional Features'], ['On the Ear', 'JBL', 'Wired', 'PC, Laptops, MP3 Player, CD Player, iPhones, iPod, iPad, Tablet', 'Over the Head (Supra-aural), Closed Back', 'J03B Tempo', 'Black', 'Powerful Clear JBL Sound', '40 mm', '20 - 20000 Hz', '1 Year Domestic Carry In Limited Warranty', 'Carry In', 'Audio Out Plug', '3.5 mm', 'Gold Plated', '1.2 m', 'Adjustable Padded Headband, Self Adjusting Earcup Alignment, Fold Flat Earcups'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['SoundMAGIC ES 18 Headphone'], [' Rs. 679 '], ['24% OFF'], [' Rs. 899 '], ['4.4'], ['748'], ['1929'], ['Other Performance Features', 'Sensitivity', 'Impedance', 'Headphone Driver Units', 'Frequency Response', 'Headset Design', 'Brand', 'Wired/Wireless', 'Headphone Type', 'Model ID', 'Magnet Type', 'Color', 'In Sales Package', 'Warranty Summary', 'Weight', 'Headphone Jack', 'Connector Plating', 'Cord Type'], ['Noise Isolation, Hi-Fi Sound, High Frequency Bright, Accurate Reduction', '100 dB/mW (Power On)', '16 ohm (Power On)', '10 mm', '15 - 22000 Hz', 'In the Ear', 'SoundMAGIC', 'Wired', 'In-the-ear', 'ES 18', 'Neodymium', 'Red & Black', 'Headphone, User Guide', '6 Months Manufacturer Warranty.', '11 g', '3.5 mm', 'Gold Plated', '1.2 m'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['HP H1000 Headphones'], [' Rs. 369 '], ['38% OFF'], [' Rs. 599 '], ['4.2'], ['319'], ['828'], ['Frequency Response', 'Headset Design', 'Brand', 'Wired/Wireless', 'Compatible Devices', 'Headphone Type', 'Model ID', 'Color', 'In Sales Package', 'Warranty Summary', 'Weight', 'Headphone Jack', 'Additional Features'], ['20 - 20000 Hz', 'In the Ear', 'HP', 'Wired', 'Laptop', 'Canalphone', 'H1000', 'Black', 'H2C23AA In-Ear Headphone', '1 Year Domestic Warranty', '14 g', '3.5 mm', 'Booming Bass, Clean and Crisp Sounding Audio'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Sennheiser MX 170 Earphones'], [' Rs. 586 '], ['15% OFF'], [' Rs. 690 '], ['4.4'], ['685'], ['1680'], ['Headset Design', 'Brand', 'Wired/Wireless', 'Headphone Type', 'Model ID', 'Color', 'Other Performance Features', 'Sensitivity', 'Impedance', 'Frequency Response', 'Weight', 'Warranty Summary', 'Headphone Jack', 'Cord Type', 'Additional Features'], ['In the Ear', 'Sennheiser', 'Wired', 'Earbud', 'MX 170', 'Black', 'Bass-driven Stereo Sound, Dynamic Speaker System', '109 dB/mW (Power On)', '32 ohm (Power On)', '22 - 20000 Hz', '14 g', '2 Years Warranty', '3.5 mm', '1.2 m Symmetric Cord', 'Tangle-free Listening'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Tekfusion - Twinwoofers In-Ear Headphones Black Chrome Edition'], [' Rs. 1,162 '], ['25% OFF'], [' Rs. 1,550 '], ['3.7'], ['1,077'], ['4105'], ['Headset Design', 'Brand', 'Wired/Wireless', 'Headphone Type', 'Model ID', 'Color', 'Other Performance Features', 'Sensitivity', 'Impedance', 'Frequency Response', 'Weight', 'Warranty Summary', 'Headphone Jack', 'Connector Plating', 'Cord Type', 'Additional Features'], ['In the Ear', 'Tekfusion', 'Wired', 'Canalphone', 'Twinwoofers', 'Black', 'Blocks Ambient Noise, Noise Isolating Capability', '113 dB/mW (Power On)', '16 ohm (Power On)', '19 - 21 Hz', '30 g', '1 Year', '3.5 mm', 'Gold Plated', '1.2 m Symmetric Cord', 'Ergonomic Housing, Built-in HD Dynamic Speaker, Compatible with Ipod Touch 2nd Generation'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['SoundMAGIC ES 18 Headphone'], [' Rs. 563 '], ['37% OFF'], [' Rs. 899 '], ['4.4'], ['748'], ['1929'], ['Other Performance Features', 'Sensitivity', 'Impedance', 'Headphone Driver Units', 'Frequency Response', 'Headset Design', 'Brand', 'Wired/Wireless', 'Headphone Type', 'Model ID', 'Magnet Type', 'Color', 'In Sales Package', 'Warranty Summary', 'Weight', 'Headphone Jack', 'Connector Plating', 'Cord Type'], ['Noise Isolation, Hi-Fi Sound, High Frequency Bright, Accurate Reduction', '100 dB/mW (Power On)', '16 ohm (Power On)', '10 mm', '15 - 22000 Hz', 'In the Ear', 'SoundMAGIC', 'Wired', 'Canalphone', 'ES 18', 'Neodymium', 'Black & Silver', 'Headphone, User Guide', '6 Months Manufacturer Warranty.', '11 g', '3.5 mm', 'Gold Plated', '1.2 m'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Sony MDR-ZX110 Wired Headphones'], [' Rs. 775 '], ['44% OFF'], [' Rs. 1,399 '], ['4.1'], ['113'], ['290'], ['Headset Design', 'Brand', 'Wired/Wireless', 'Headphone Type', 'Model ID', 'In Sales Package', 'Color', 'Sensitivity', 'Impedance', 'Headphone Driver Units', 'Frequency Response', 'Weight', 'Warranty Summary', 'Connector Plating', 'Cord Type', 'Additional Features'], ['On the Ear', 'Sony', 'Wired', 'Over the Head (Supra-aural), Closed Back', 'MDR-ZX110', 'Headphone, Warranty Card', 'White', '98 dB/mW (Power On)', '24 ohm (Power On)', '30 mm', '12 - 22000 Hz', '120 g (without cord)', '6 Months Manufacturers Warranty', 'Gold Plated', '1.2 m', 'Dynamic Type, L-shaped Stereo Mini Plug'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Philips SHM1900/97 Wired Headphones'], [' Rs. 445 '], ['18% OFF'], [' Rs. 549 '], ['4.2'], ['995'], ['2664'], ['Headset Design', 'Brand', 'Wired/Wireless', 'Headphone Type', 'Model ID', 'Color', 'Magnet Type', 'Other Performance Features', 'Sensitivity', 'Impedance', 'Headphone Driver Units', 'Frequency Response', 'Weight', 'Width x Height x Depth', 'Warranty Summary', 'Headphone Jack', 'Connector Plating', 'Cord Type', 'Additional Features'], ['Over the Ear', 'Philips', 'Wired', 'Over the Head (Circumaural), Closed Back', 'SHM1900/97', 'Black', 'Neodymium', 'Optimize Sound Quality and Bass Response', '98 dB/mW (Power On)', '32 ohm (Power On)', '40 mm', '20 - 20000 Hz', '200 g', '95 x 215 x 196 mm', '6 Months Warranty', '3.5 mm', 'Chrome Plated', '2 m One-sided Copper Cord', 'Adjustable Headband, Lightweight Design'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Sony MDR-G45LP/Q(IN) Wired Headphones'], [' Rs. 850 '], ['4% OFF'], [' Rs. 890 '], ['4'], ['280'], ['884'], ['Other Performance Features', 'Sensitivity', 'Headphone Driver Units', 'Frequency Response', 'Headset Design', 'Brand', 'Wired/Wireless', 'Headphone Type', 'Model ID', 'Color', 'Magnet Type', 'Warranty Summary', 'Weight', 'Headphone Jack', 'Connector Plating', 'Cord Type', 'Additional Features'], ['Noise Canceling Feature', '104 dB/mW (Power On)', '30 mm', '16 - 20000 Hz', 'On the Ear', 'Sony', 'Wired', 'Over the Head (Supra-aural), Closed Back', 'MDR-G45LP/Q(IN)', 'Black', 'Neodymium', '6 Months Warranty', '55 g (without cord)', '3.5 mm', 'Gold Plated', '1.2 m', 'Power Handling Capacity: 100 mW, Portable Audio System, L-shaped Plug, Foldable, Dynamic Headphones Technology, Stereo Sound Output Mode, Diaphragm: PET - 1.2 inch, Retractable Cord Function, Pressure Relieving Urethane Cushion'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Sony MDR-XB30EX Extra-Bass Stereo Headphone'], [' Rs. 1,717 '], ['31% OFF'], [' Rs. 2,490 '], ['4.5'], ['745'], ['1952'], ['Headset Design', 'Brand', 'Wired/Wireless', 'Headphone Type', 'Model ID', 'In Sales Package', 'Color', 'Magnet Type', 'Maximum Power Input', 'Other Performance Features', 'Sensitivity', 'Impedance', 'Headphone Driver Units', 'Frequency Response', 'Weight', 'Warranty Summary', 'Connector Plating', 'Cord Type', 'Additional Features'], ['In the Ear', 'Sony', 'Wired', 'Canalphone', 'XB-30', 'Headphone, Carry Case', 'Black', 'Neodymium', '100 mW', 'Intense Bass and Ultra Clear Mid-range Sounds', '105 dB/mW (Power On)', '16 ohm (Power On)', '13.5 mm', '4 - 24000 Hz', '8 g (without cord)', '1 Year', 'Gold Plated', 'Y-shape Cord', 'L-shaped Stereo Mini Plug, Dynamic Type, Hybrid Silicone Rubber Earbuds, Fitting Assist, Vertical in-ear, Tangle-free Serrated Cord, PET Diaphragm'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Sennheiser HD 202 II'], [' Rs. 2,090 '], ['8% OFF'], [' Rs. 2,290 '], ['4.5'], ['311'], ['906'], ['Other Performance Features', 'Sensitivity', 'Impedance', 'Frequency Response', 'Headset Design', 'Brand', 'Wired/Wireless', 'Headphone Type', 'Model ID', 'Magnet Type', 'Color', 'Warranty Summary', 'Weight', 'Width x Height x Depth', 'Headphone Jack', 'Cord Type', 'Additional Features'], ['Total Harmonic Distortion (THD): 0.5 %', '115 dB/mW (Power On)', '32 ohm (Power On)', '18 - 18000 Hz', 'Over the Ear', 'Sennheiser', 'Wired', 'Over the Head (Supra-aural), Closed Back', 'HD 202 II', 'Neodymium', 'Black', '2 Years Warranty', '396 g / 130 g (without cord)', '203 x 248 x 76 mm', '3.5 mm, 6.3 mm', '3 m', 'Powerful Bass Response, Lightweight and Comfortable, Rugged and Flexible Headband, Good Attenuation of Ambient Noise, Ultra-lightweight, Replaceable Leatherette Ear Cushions'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Skullcandy S2DUDZ-003 Headphones'], [' Rs. 580 '], ['22% OFF'], [' Rs. 749 '], ['3.7'], ['419'], ['1427'], ['Headset Design', 'Brand', 'Headphone Type', 'Model ID', 'Warranty Summary'], ['In the Ear', 'Skullcandy', 'Canalphone', 'S2DUDZ-003', '1 Year Manufacturer Warranty.'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Philips SHP2000'], [' Rs. 649 '], [], [], ['3.8'], ['308'], ['761'], ['Other Performance Features', 'Maximum Power Input', 'Sensitivity', 'Impedance', 'Headphone Driver Units', 'Frequency Response', 'Headset Design', 'Brand', 'Wired/Wireless', 'Compatible Devices', 'Headphone Type', 'Model ID', 'Warranty Summary', 'Weight', 'Width x Height x Depth', 'Headphone Jack', 'Connector Plating', 'Cord Type', 'Additional Features'], ['Deep Bass, Optimize Sound Quality and Bass Response', '500 mW', '96 dB/mW (Power On)', '32 ohm (Power On)', '40 mm', '15 - 22000 Hz', 'Over-the-head', 'Philips', 'Wired', 'Music, PC, TV', 'Over the Head (Circumaural), Open Back', 'SHP2000/97', '6 Months limited Warranty Philips India Warranty and Free Transit Insurance', '0.226 kg', '107 x 208 x 196 mm', '3.5 mm, 6.3 mm', 'Chrome Plated', '2 m Optical Fiber Cable Cord', 'Full Size Design, Comfort Ear Cushions, Easy Adjustable Headband, Lightweight Headband'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Sony MDR-XB400/BQE Headphones'], [' Rs. 2,299 '], ['4% OFF'], [' Rs. 2,399 '], ['4.5'], ['374'], ['1082'], ['Headset Design', 'Brand', 'Wired/Wireless', 'Series', 'Headphone Type', 'Model ID', 'Color', 'Maximum Power Input', 'Sensitivity', 'Impedance', 'Headphone Driver Units', 'Frequency Response', 'Weight', 'Covered in Warranty', 'Warranty Summary', 'Not Covered in Warranty', 'Connector Plating', 'Cord Type', 'Additional Features'], ['Over the Ear', 'Sony', 'Wired', 'XB', 'Over the Head (Supra-aural), Closed Back', 'MDR-XB400/BQE', 'Black', '1000 mW', '100 dB/mW (Power On)', '24 ohm (Power On)', '30 mm', '5 - 22000 Hz', '150 g (without cord)', 'Dead on Arrival, Damage, Defective', '1 Year Domestic Warranty', 'Forceful Tampering', 'Gold Plated', '1.2 m Y - Type Cord', 'CCAW Voice Coil'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])

#[ 'name',  'cost',  "discount",  "originalPrice",  "ratings",  "noReviews",  "votes",  "speckey",  "specvalue",  'ImageURL' ]
=======
full = []

full.append([['Sennheiser CX 180 Street II In-ear-canalphone'], [' Rs. 841 '], ['15% OFF'], [' Rs. 990 '], ['4.3'], ['872'], ['2021'], ['Headset Design', 'Brand', 'Wired/Wireless', 'Controls', 'Headphone Type', 'Model ID', 'Other Performance Features', 'Sensitivity', 'Impedance', 'Frequency Response', 'Weight', 'Warranty Summary', 'Cord Type'], ['In-ear-canalphone', 'Sennheiser', 'Wired', 'Innovative Finger-Contoured', 'In-the-ear', 'CX 180', 'Bass-driven Stereo Sound, High Passive Attenuation of Ambient Noise, Active Noise Cancellation', '110 dB/mW (Power On)', '16 ohm (Power On)', '20 - 20000 Hz', '5 g', '2 Years Warranty', '1.2 m Symmetric Cord'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Philips SHE1360/97 Wired Headphones'], [' Rs. 111 '], [], [], ['4.2'], ['1,137'], ['3281'], ['Headset Design', 'Brand', 'Wired/Wireless', 'Headphone Type', 'Model ID', 'Color', 'Maximum Power Input', 'Other Performance Features', 'Sensitivity', 'Impedance', 'Headphone Driver Units', 'Frequency Response', 'Warranty Summary', 'Headphone Jack'], ['In the Ear', 'Philips', 'Wired', 'Earbud', 'SHE1360/97', 'Black', '50 mW', 'Bass Beat Vents for Better Sound', '100 dB/mW (Power On)', '16 ohm (Power On)', '15 mm', '16 - 20000 Hz', '6 Months Warranty', '3.5 mm'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Sennheiser HD 180'], [' Rs. 841 '], ['15% OFF'], [' Rs. 990 '], ['4'], ['447'], ['1228'], ['Headset Design', 'Brand', 'Wired/Wireless', 'Compatible Devices', 'Headphone Type', 'Model ID', 'Color', 'Frequency Response', 'Weight', 'Warranty Summary'], ['Over the Ear', 'Sennheiser', 'Wired', 'Laptops, PC, Computer, Mobile', 'Over the Head (Circumaural), Closed Back', 'HD 180', 'Black', '21 - 18000 Hz', '130 g', '2 Years Warranty Sennheiser India Warranty and Free Transit Insurance'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Creative EP-600 Headphone'], [' Rs. 339 '], ['32% OFF'], [' Rs. 499 '], ['3.6'], ['300'], ['907'], ['Headset Design', 'Brand', 'Wired/Wireless', 'Headphone Type', 'Model ID', 'Magnet Type', 'Other Performance Features', 'Sensitivity', 'Impedance', 'Headphone Driver Units', 'Frequency Response', 'Weight', 'Warranty Summary', 'Cord Type', 'Additional Features'], ['In the Ear', 'Creative', 'Wired', 'Canalphone', 'EP-600', 'Neodymium', 'Noise Isolation', '100 dB/mW (Power On)', '16 ohm (Power On)', '10 mm', '20 - 20000 Hz', '12 g', '6 Months of Manufacturer Warranty.', '1.2 m', 'Ergonomic Design, Soft Silicone Ear Bud'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Philips SBCHL140/98 Wired Headphones'], [' Rs. 239 '], ['20% OFF'], [' Rs. 299 '], ['3.7'], ['73'], ['285'], ['Other Performance Features', 'Maximum Power Input', 'Sensitivity', 'Impedance', 'Headphone Driver Units', 'Frequency Response', 'Headset Design', 'Brand', 'Wired/Wireless', 'Headphone Type', 'Model ID', 'Magnet Type', 'Color', 'Warranty Summary', 'Headphone Jack', 'Connector Plating', 'Cord Type', 'Additional Features'], ['Air Vents for Rich Deep Sound', '100 mW', '96 dB/mW (Power On)', '32 ohm (Power On)', '30 mm', '18 - 20000 Hz', 'On the Ear', 'Philips', 'Wired', 'Over the Head (Supra-aural), Closed Back', 'SBCHL140/98', 'Ferrite', 'Graphite', '6 Months Warranty', '3.5 mm', 'Chrome Plated', '1 m Two-Parallel Symmetric- Copper Cord', 'Ultra Lightweight , Reinforced Cable Connection'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['Creative EP-630 earphone In-the-ear Headphone'], [' Rs. 575 '], ['42% OFF'], [' Rs. 999 '], ['4.4'], ['775'], ['2312'], ['Headset Design', 'Brand', 'Headphone Type', 'Model ID', 'Warranty Summary'], ['Ear Bud', 'Creative', 'Earbud', 'CR EP-630', '6 months Creative India warranty.'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])
full.append([['JBL J03B Tempo Wired Headphones'], [' Rs. 3,000 '], ['11% OFF'], [' Rs. 3,400 '], ['4.4'], ['980'], ['2620'], ['Headset Design', 'Brand', 'Wired/Wireless', 'Compatible Devices', 'Headphone Type', 'Model ID', 'Color', 'Other Performance Features', 'Headphone Driver Units', 'Frequency Response', 'Warranty Summary', 'Warranty Service Type', 'Power Supply', 'Headphone Jack', 'Connector Plating', 'Cord Type', 'Additional Features'], ['On the Ear', 'JBL', 'Wired', 'PC, Laptops, MP3 Player, CD Player, iPhones, iPod, iPad, Tablet', 'Over the Head (Supra-aural), Closed Back', 'J03B Tempo', 'Black', 'Powerful Clear JBL Sound', '40 mm', '20 - 20000 Hz', '1 Year Domestic Carry In Limited Warranty', 'Carry In', 'Audio Out Plug', '3.5 mm', 'Gold Plated', '1.2 m', 'Adjustable Padded Headband, Self Adjusting Earcup Alignment, Fold Flat Earcups'], ['http://img1a.flixcart.com/img/thumb-default.jpg']])

#[ 'name',  'cost',  "discount",  "originalPrice",  "ratings",  "noReviews",  "votes",  "speckey",  "specvalue",  'ImageURL' ]

>>>>>>> 14ed198f8f62f9fc38c36be6c5f56242e21cb116
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
<<<<<<< HEAD
	#for j in range(0,len(full[i][7])):
	for k in range(0,len(specs)) :
		try:
			#print("found one")
			index = full[i][7].index(specs[k])
			new[i].append(full[i][8][index])
			#print(str(i)+ ":   "+ full[i][8][index])
		except:
			new[i].append("N/A")
=======
	for j in range(0,len(full[i][7])):
		for k in range(0,len(specs)) :
			try:
				#print("found one")
				index = full[i][7].index(specs[k])
				new[i].append(full[i][8][index])
				#print(str(i)+ ":   "+ full[i][8][index])
			except:
				new[i].append("N/A")
>>>>>>> 14ed198f8f62f9fc38c36be6c5f56242e21cb116


# building header
t = ''
for s in specs: 
<<<<<<< HEAD
	t += s+ '"|"'

f = open("final.csv","w")
f.write('"Product Name"|"Cost"|"Discount"|"MRP"|"Ratings"|"noReviews"|"votes"|"'+ t+'"|ImageURL"')
=======
	t += s+ "|"

f = open("final.txt","a")
f.write('"name"|"cost"|"discount"|"originalPrice"|"ratings"|"noReviews"|"votes"|"speckey"|"specvalue"|"ImageURL"')
>>>>>>> 14ed198f8f62f9fc38c36be6c5f56242e21cb116


for i in range(0,len(new)):
	f.write("\n")
<<<<<<< HEAD
	for j in range(0,len(new[i])):
		#print(j)
		f.write(filterst(str(new[i][j]),j)+"|")
# for row in new: 
# 	f.write("\n"+ str(row))

f.close()


=======
	for j in new[i]:
		#print(j)
		f.write(str(j)+"|")
# for row in new: 
# 	f.write("\n"+ str(row))

>>>>>>> 14ed198f8f62f9fc38c36be6c5f56242e21cb116



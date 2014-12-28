0------				1
1------				http://magicbricks.com/propertyDetails/3-BHK-700-Sq-ft-Builder-Floor-Apartment-FOR-Sale-Uttam-Nagar-in-New-Delhi&id=ZtgMMpzJap5zpSvf+uAgZw==
2------				['\n3 BHK, 700 Sq-ft Builder Floor Apartment For Sale\n']
3------				['\n26.0 Lac(s)\n']   	--- filter /n and split on space 
4------				['3,714/Sq-ft)']   		--- filter '), split on / 
5------				['15 %\n']				--- filter \n%'
6------				[" Dec 28, '14 "]		--- filter "
7------				['RO Water System', 'Vaastu Compliant', 'Intercom Facility', 'Reserved Parking', 'Waste Disposal', 'Park', 'Security', 'Water Storage', 'Lift', 'Power Back Up', 'Rain Water Harvesting']
8------				[['Address'], ['Bedrooms'], ['Bathrooms'], ['Balconies'], ['Furnished'], ['Possession Status'], ['Floor Number'], ['Total Floors'], ['Units on the Floor '], ['Covered Area '], ['Carpet/Builtup Area '], ['Additional Rooms '], ['Facing '], ['Overlooking '], ['Age of Construction '], ['Transaction Type '], ['Type of Ownership '], ['Units Available ']]
9------				[['uttam nagar, New Delhi, Uttam Nagar, New Delhi - West - 110059'], ['3'], ['2'], ['1'], ['Semi-Furnished'], ['Ready to Move'], ['1 '], ['4 '], ['2 '], ['700'], ['690'], ['Puja Room'], ['East '], ['Main Road '], ['New Construction'], ['New Property'], ['Freehold'], ['2']]


def tester(st,j):
	remove = []
	split = None
	if j == 2 or j == 3 or j == 4 or j == 5: 
		remove.append('\n')
		remove.append("'")
		remove.append('%')
		remove.append(')')

	if j == 3: 
		split = " "
	if j == 4:
		split = "/"


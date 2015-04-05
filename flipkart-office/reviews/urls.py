import requests,os,random
from lxml import etree
from urlparse import urlparse
var = []
current = os.getcwd()
var.append(["(86 ratings)","http://img6a.flixcart.com/image/book/5/6/0/jee-main-physics-in-just-40-days-200x200-imadpgupzeatzht9.jpeg","JEE Main Physics in Just 40 Days (English) 4th Edition (Paperback)","/jee-main-physics-just-40-days-english-4th/p/itmdpgq8fgjwsun8?pid=9789351410560&srno=b_21&ref=d6aca026-9777-462f-893c-e96c5ff24f0d","Rs. 300","Saurabh A."])
var.append(["(140 ratings)","http://img5a.flixcart.com/image/book/8/1/2/organic-chemistry-for-jee-main-advanced-200x200-imae6fm9axxcgwbm.jpeg","Organic Chemistry for JEE - Main & Advanced (English) 1st Edition (Paperback)","/organic-chemistry-jee-main-advanced-english-1st/p/itmdkprvzqyaexmb?pid=9788126541812&srno=b_22&ref=d6aca026-9777-462f-893c-e96c5ff24f0d","Rs. 595","Solomons ; Fryhle"])
var.append(["(20 ratings)","http://img5a.flixcart.com/image/book/2/8/7/jee-main-chemistry-in-40-days-a-revision-cum-crash-course-2015-200x200-imaeythxuvt7yvcx.jpeg","JEE Main Chemistry in 40 Days a Revision cum Crash Course 2015 (English) 5th Edition (Paperback)","/jee-main-chemistry-40-days-revision-cum-crash-course-2015-english-5th/p/itmeyp3wdtkpzqan?pid=9789351762287&srno=b_23&ref=d6aca026-9777-462f-893c-e96c5ff24f0d","Rs. 258","Dr. Praveen Kumar"])
var.append(["(88 ratings)","http://img6a.flixcart.com/image/book/4/2/9/play-with-graphs-for-jee-main-advanced-200x200-imadv9kfuuqhgmx7.jpeg","Play with Graphs for JEE Main & Advanced (English) 7th Edition (Paperback)","/play-graphs-jee-main-advanced-english-7th/p/itmdv8y2apnuzfsp?pid=9789351418429&srno=b_24&ref=d6aca026-9777-462f-893c-e96c5ff24f0d","Rs. 176","Amit M Agarwal"])
var.append(["(285 ratings)","http://img5a.flixcart.com/image/book/4/1/5/modern-approach-to-chemical-calculations-mukherjee-200x200-imaddts9zuyzazff.jpeg","Modern Approach to Chemical Calculations PB (English) (Paperback)","/modern-approach-chemical-calculations-pb-english/p/itmdyufk76hgeg6h?pid=9788177096415&srno=b_25&ref=d6aca026-9777-462f-893c-e96c5ff24f0d","Rs. 240","Mukherjee"])
var.append(["(31 ratings)","http://img6a.flixcart.com/image/book/4/5/7/sail-steel-authority-of-india-limited-management-trainee-technical-recruitment-examination-electrical-engineering-including-practice-paper-200x200-imadjhtzfszuxqt5.jpeg","SAIL Management Trainee(Technical) Recruitment Examination Electrical Engineering (English) 4th Edition (Paperback)","/sail-management-trainee-technical-recruitment-examination-electrical-engineering-english-4th/p/itmdjhx2f5sh4vvh?pid=9788183558457&srno=b_26&ref=d6aca026-9777-462f-893c-e96c5ff24f0d","Rs. 650","G K P"])
var.append(["(10 ratings)","http://img6a.flixcart.com/image/book/2/7/0/jee-main-physics-in-40-days-a-revision-cum-crash-course-2015-200x200-imaeythxg5q5r8nx.jpeg","JEE Main Physics in 40 Days a Revision cum Crash Course 2015 (English) 5th Edition (Paperback)","/jee-main-physics-40-days-revision-cum-crash-course-2015-english-5th/p/itmeyp3xtqmt4mg7?pid=9789351762270&srno=b_27&ref=d6aca026-9777-462f-893c-e96c5ff24f0d","Rs. 258","Saurabh A."])
var.append(["(14 ratings)","http://img6a.flixcart.com/image/book/2/9/4/jee-main-mathematics-in-40-days-a-revision-cum-crash-course-2015-200x200-imaeythxwqd5zask.jpeg","JEE Main Mathematics in 40 Days a Revision cum Crash Course 2015 (English) (Paperback)","/jee-main-mathematics-40-days-revision-cum-crash-course-2015-english/p/itmdynu5vfcfq9ne?pid=9789351762294&srno=b_28&ref=d6aca026-9777-462f-893c-e96c5ff24f0d","Rs. 258","Rajeev Manocha"])
var.append(["(60 ratings)","http://img5a.flixcart.com/image/book/8/4/7/handbook-series-of-electronics-communication-engineering-200x200-imadgzn9uuscjbpk.jpeg","Electronics and Communication Engineering (English) (Paperback)","/electronics-communication-engineering-english/p/itmdgxfw5uw4mqhp?pid=9789350943847&srno=b_29&ref=d6aca026-9777-462f-893c-e96c5ff24f0d","Rs. 198","Experts Compilation"])
var.append(["(45 ratings)","http://img6a.flixcart.com/image/book/1/9/3/formulae-at-finger-tips-mathematics-formulae-definitions-200x200-imaey8hzry5ph6sj.jpeg","Formulae At Finger Tips Mathematics (Formulae, Definitions, Equations Dictionary) (English) (Paperback)","/formulae-finger-tips-mathematics-formulae-definitions-equations-dictionary-english/p/itmdyur3kyxpzmff?pid=9788183553193&srno=b_30&ref=d6aca026-9777-462f-893c-e96c5ff24f0d","Rs. 68","Narayana, D.|author;"])
var.append(["(354 ratings)","http://img6a.flixcart.com/image/book/1/5/8/elementary-algebra-for-school-200x200-imae2m87gvzjgk6u.jpeg","Problems in General Physics (English) (Paperback)","/problems-general-physics-english/p/itme5pgdfyfuqsjb?pid=9788183552158&srno=b_31&ref=d6aca026-9777-462f-893c-e96c5ff24f0d","Rs. 77","IRODOV"])
var.append(["(39 ratings)","http://img6a.flixcart.com/image/book/4/8/1/skills-in-mathematics-differential-calculus-for-jee-main-200x200-imadv9kfftgqpmn5.jpeg","Skills in Mathematics Differential Calculus for JEE Main & Advanced (English) 7th Edition (Paperback)","/skills-mathematics-differential-calculus-jee-main-advanced-english-7th/p/itmdv8y2mqyjb4fv?pid=9789351418481&srno=b_32&ref=d6aca026-9777-462f-893c-e96c5ff24f0d","Rs. 470","Amit M Agarwal"])
var.append(["(52 ratings)","http://img6a.flixcart.com/image/book/6/1/7/hand-book-of-mechanical-engineering-200x200-imadkefzcjgddywd.jpeg","Hand Book of Mechanical Engineering PB (English) 2014 Edition (Paperback)","/hand-book-mechanical-engineering-pb-english-2014/p/itmdkgpupwsfyh2a?pid=9788183558617&srno=b_33&ref=d6aca026-9777-462f-893c-e96c5ff24f0d","Rs. 80","GKP"])
var.append(["(43 ratings)","http://img5a.flixcart.com/image/book/9/2/9/mathematics-for-joint-entrance-examination-advanced-calculus-200x200-imaduwc7tsgb5ydr.jpeg","Mathematics for Joint Entrance Examination (Advanced) - Calculus (English) 2nd Edition (Paperback)","/mathematics-joint-entrance-examination-advanced-calculus-english-2nd/p/itm9788131522929?pid=9788131522929&srno=b_34&ref=d6aca026-9777-462f-893c-e96c5ff24f0d","Rs. 470","Tewani"])
var.append(["(174 ratings)","http://img6a.flixcart.com/image/book/5/7/6/problems-plus-in-iit-mathematics-200x200-imad8hz2fbznytmp.jpeg","Problems Plus In IIT Mathematics (English) (Paperback)","/problems-plus-iit-mathematics-english/p/itmdyufkwbpcarfa?pid=9788177096576&srno=b_35&ref=d6aca026-9777-462f-893c-e96c5ff24f0d","Rs. 480","A Das gupta"])
var.append(["(19 ratings)","http://img5a.flixcart.com/image/book/9/6/7/physics-for-joint-entrance-examination-advanced-mechanics-2-200x200-imaduwc72qgnrh8v.jpeg","Physics for Joint Entrance Examination (Advanced) - Mechanics 2 (English) 2nd Edition (Paperback)","/physics-joint-entrance-examination-advanced-mechanics-2-english-2nd/p/itm9788131522967?pid=9788131522967&srno=b_36&ref=d6aca026-9777-462f-893c-e96c5ff24f0d","Rs. 438","Sharma"])
var.append(["(47 ratings)","http://img5a.flixcart.com/image/book/4/4/3/skills-in-mathematics-integral-calculus-for-jee-main-advanced-200x200-imadv9kf7p2xtucp.jpeg","Skills in Mathematics Integral Calculus for JEE Main & Advanced (English) 7th Edition (Paperback)","/skills-mathematics-integral-calculus-jee-main-advanced-english-7th/p/itmdv8y27n2vphgj?pid=9789351418443&srno=b_37&ref=d6aca026-9777-462f-893c-e96c5ff24f0d","Rs. 199","Amit M Agarwal"])
var.append(["(17 ratings)","http://img5a.flixcart.com/image/book/9/7/4/physics-for-joint-entrance-examination-advanced-waves-and-200x200-imaduwc7wrzverny.jpeg","Physics for Joint Entrance Examination (Advanced) - Waves and Thermodynamics (English) 2nd Edition (Paperback)","/physics-joint-entrance-examination-advanced-waves-thermodynamics-english-2nd/p/itmdzkkwt6qvyj2z?pid=9788131522974&srno=b_38&ref=d6aca026-9777-462f-893c-e96c5ff24f0d","Rs. 424","Sharma"])
var.append(["(20 ratings)","http://img6a.flixcart.com/image/regionalbooks/b/x/b/physics-iit-jee-aieee-neet-set-of-2-volumes-for-2015-200x200-imadycnqvgayzuhs.jpeg","Physics - Errorless 100 Solved Objective Practice Book (Set Of 2 Volumes) (Paperback)","/physics-errorless-100-solved-objective-practice-book-set-2-volumes/p/itmdyd3rhygwwymz?pid=RBKDY2ZDASHJJBXB&srno=b_39&ref=d6aca026-9777-462f-893c-e96c5ff24f0d","Rs. 1236",""])

def urlconvertor(url): 
	return(	'http://www.flipkart.com'+url.replace('/p/','/product-reviews/')) 
ini = "//div[@class='fclear fk-review fk-position-relative line ']"
dictionary = {
	"Star":"/div[@class='unit size1of5 section1']/div[@class='line'][1]/div[@class='fk-stars']/@title",
	"reviewHeading":"/div[@class='lastUnit size4of5 section2']/div[@class='line fk-font-normal bmargin5 dark-gray']/strong/text()",
	"reviewDescription":"/div[@class='lastUnit size4of5 section2']/p[@class='line bmargin10']/span[@class='review-text']/text()",
	"reviewerName":"/div[@class='unit size1of5 section1']/div[@class='line'][2]/a[@class='load-user-widget fk-underline']/text()",
	"reviewDate":"/div[@class='unit size1of5 section1']/div[@class='date line fk-font-small']/text()"
}
remove = ['\\xa0','\\t',"u'",'"',"\\n","\\r","'",'[',']','  ']
f = open('reviews.csv','w')
f.close()
counter = 0 
for i in var:
	url = i[3]
	url = urlconvertor(url)
	# print url
	try:
		t = requests.get(url)
		counter += 1
		print(str(counter*100/len(var))+'% Completed')
	except: 
		print "FAILED: " + url
		pass
	tree= etree.HTML(t.text)
	overallRating = tree.xpath("//div[@class='pp-big-star']")
	items = tree.xpath(ini)
	# print '================='+str(len(items))+'=================='
	productReviews = []	
	for item in range(0,len(items)):  
		review  = []
		# print '------------------------'
		for key in dictionary:				
			xpath = ini + "["+str(item+1)+"]"+dictionary[key]
			out = (tree.xpath(xpath))			
			if len(out)> 1: 
				temp = ''
				for i in out:
					temp += i#+'\n'
				out = temp 

			out = str(out)
			if key == 'Star':
				out = out.replace(' star','')
				out = out.replace('s','')

			for rem in remove: 
				while rem in out: 
					out = (out.replace(rem,' ')).strip()
			# print key + '\t\t\t\t: '+out 
			if key == "reviewDescription":
				os.chdir(current+ '\\reviews')
				name = urlparse(url)
				params = (name.query).split('&')
				for param in params:
					if 'pid' in param: 
						fname = param.replace('pid=','')
				fname += "_"+str(item)
				f = open(fname+".txt",'w')
				f.write(out)
				f.close()
				os.chdir(current)
				out = fname
			review.append(out)
		review.append(url)
		# productReviews.append(review)
		f = open('reviews.csv','a')
		f.write('\n')
		for out in review:
			f.write('"'+out+'",')
		f.close()


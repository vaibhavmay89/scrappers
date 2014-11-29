from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
nop = 0 
url = "http://www.flipkart.com/mobiles/pr?p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&sid=tyy%2C4io&ref=dc51ee0b-3309-40ab-8c0f-4e7fcd11620d"
#url = "http://www.flipkart.com/sports-fitness/fitness-accessories/ab-exercisers/pr?p[]=sort=popularity&sid=dep,xnh,abo&otracker=nmenu_sub_more-stores_0_Ab%20Exercisers"
driver = webdriver.Chrome()
driver.get(url)
fname = 'mobiles.txt'

items = []
def collector():
	
	global items, driver, f
	items = driver.find_elements_by_xpath("//div[@class='pu-title fk-font-13']/a[@class='fk-display-block']")
	urls = []
	for i in items: 		
		j = i.get_attribute("href")
		k = ("\n"+str(j))
		urls.append(k)
	urls = set(urls)
	f = open(fname,"w")
	f.write("\n")

	for i in urls: 
		f.write(str(i))
	f.close()


def scrollToAction():
	
	load = """$("#load-more-results").animate({scrollTop: $("#load-more-results").offset().top - 300}, 5000);"""
	show = """$("body").animate({scrollTop: $("#show-more-results").offset().top - 300}, 5000);"""
	seo = '''$("body").animate({scrollTop: $(".fk-footer-ssa").offset().top - 800}, 100);'''
	# print("Scroller called")
	

	try:
		driver.execute_script(seo)
	except:
		try:
			print("load didnt work trying show")
			driver.execute_script(show)
		except:
			try:
				print("SHOW didnt work trying SEO")
				driver.execute_script(seo)
			except:
				print("Ain't scrolling nowhere")
	time.sleep(2)
	collector()



#driver.save_screenshot('screenshot.png')
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# seeMore = driver.findElement(By.id("show-more-results"))

# driver.execute_script("$('html, body').animate({scrollTop: $('#show-more-results').offset().top - 100}, 2000);")
# try:
# 	driver.execute_script("$('html, body').animate({scrollTop: $('#load-more-results').offset().top - 100}, 2000);")
# except:
# 	driver.execute_script("$('html, body').animate({scrollTop: $('#show-more-results').offset().top - 100}, 2000);")
noMore = driver.find_elements_by_xpath("//div[@id='no-more-results']")
scrollToAction()
while (noMore[0].get_attribute("style") != "display: block;"):
	# print("1:")
	scrollToAction()
	if(driver.find_elements_by_xpath("//div[@id='show-more-results']")[0].get_attribute("style") != "display: block;"):
		# print("3:")
		scrollToAction()
		time.sleep(2)
	else:
		scrollToAction()
		# print('found show more')
		element = driver.find_elements_by_xpath("//div[@id='show-more-results']")[0]
		time.sleep(2)
		try:
			driver.execute_script('$("#show-more-results").click()')
			scrollToAction()
			nop += 1 
			print ("Pressed Show More "+str(nop)+ " times")
		except:
			print("js Didnt work")
			try:
				element.click()
				nop += 1 
				print ("Pressed Show More "+str(nop)+ " times")
				scrollToAction()
			except:
				print("Sel didnt work")


	noMore = driver.find_elements_by_xpath("//div[@id='no-more-results']")
	# print("2:")
	scrollToAction()
	# time.sleep(2)
urls = []

items = driver.find_elements_by_xpath("//div[@class='pu-title fk-font-13']/a[@class='fk-display-block']")
for i in items: 
	j = i.get_attribute("href")
	k = ("\n"+str(j))
	urls.append(k)
	f.write(k)




driver.close()



# <div id="load-more-results" class="dont-show"
#//div[@class='pu-title fk-font-13']/a[@class='fk-display-block']
#//div[@id='page-2']/div[@class='gd-row browse-grid-row']/div[@class='gd-col gu3']/div[@class=' product-unit unit-4  browse-product  ']/div[@class='pu-details lastUnit']/div[@class='pu-title fk-font-13']/a[@class='fk-display-block']
# <div id="show-more-results" class="dont-show" style="display: block;">
#     Show more results
# </div>
# 
#<div id="no-more-results" class="dont-show" style="display: none;">
#     No more results to display.
# </div>

#&start=56&ref=a1e7f57b-40e5-45f5-a798-f8d424ae9388&ajax=true

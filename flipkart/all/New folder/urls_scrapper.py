from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = "http://www.flipkart.com/laptops/pr?p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&sid=6bo%2Cb5g&ref=8e05e452-7208-4feb-8c69-c3390b1bb5c3"
#url = "http://www.flipkart.com/sports-fitness/fitness-accessories/ab-exercisers/pr?p[]=sort=popularity&sid=dep,xnh,abo&otracker=nmenu_sub_more-stores_0_Ab%20Exercisers"
driver = webdriver.Chrome()
driver.get(url)

f = open("laptops.txt","w")


#driver.save_screenshot('screenshot.png')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
loadMore = driver.find_elements_by_xpath("//div[@id='no-more-results']")
while (loadMore[0].get_attribute("style") != "display: block;"):
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	if(driver.find_elements_by_xpath("//div[@id='show-more-results']")[0].get_attribute("style") != "display: block;"):
		time.sleep(2)
	else:
		print('hghg')
		element = driver.find_elements_by_xpath("//div[@id='show-more-results']")[0]
		element.click()
		try:
			element.click()
		except:
			print("first attempt worked")
		try:
			element.click()
		except:
			print("2nd attempt worked")


	loadMore = driver.find_elements_by_xpath("//div[@id='no-more-results']")
	time.sleep(2)
urls = []

items = driver.find_elements_by_xpath("//div[@class='pu-title fk-font-13']/a[@class='fk-display-block']")
for i in items: 
	j = i.get_attribute("href")
	k = ("http://wwww.flipkart.com"+ str(j))
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

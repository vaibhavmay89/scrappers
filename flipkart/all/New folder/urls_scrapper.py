from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = "http://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=ch_vn_mobile_filter_Top%20Brands_All"
#url = "http://www.flipkart.com/sports-fitness/fitness-accessories/ab-exercisers/pr?p[]=sort=popularity&sid=dep,xnh,abo&otracker=nmenu_sub_more-stores_0_Ab%20Exercisers"
driver = webdriver.Firefox()
driver.get(url)




driver.save_screenshot('screenshot.png')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
loadMore = driver.find_elements_by_xpath("//div[@id='no-more-results']")
while (loadMore[0].get_attribute("style") != "display: block;"):
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	if(driver.find_elements_by_xpath("//div[@id='show-more-results']")[0].get_attribute("style") != "display: block;"):
		time.sleep(5)
	else:
		print('hghg')
		element = driver.find_elements_by_xpath("/html/body")[0]
		element.click()


	loadMore = driver.find_elements_by_xpath("//div[@id='no-more-results']")
	time.sleep(5)




driver.close()



# <div id="load-more-results" class="dont-show"
#
#
# <div id="show-more-results" class="dont-show" style="display: block;">
#     Show more results
# </div>
# 
#<div id="no-more-results" class="dont-show" style="display: none;">
#     No more results to display.
# </div>

#&start=56&ref=a1e7f57b-40e5-45f5-a798-f8d424ae9388&ajax=true

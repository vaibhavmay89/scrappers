from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "http://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=ch_vn_mobile_filter_Top%20Brands_All"
driver = webdriver.Firefox()
driver.get(url)




driver.save_screenshot('screenshot.png')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

driver.close()



# <div id="load-more-results" class="dont-show"
#
#
# <div id="show-more-results" class="dont-show" style="display: block;">
#     Show more results
# </div>
# 
# 
# 
# 

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
# driver.get('https://rahulshettyacademy.com/angularpractice')
#
# dropdown = Select(driver.find_element_by_id('exampleFormControlSelect1'))
# dropdown.select_by_visible_text('Female') #as this female option is visible
# dropdown.select_by_index(0)
#
# driver.find_element_by_css_selector("div[class = 'form-group'] input[name= 'name']").send_keys('rahul')
# driver.find_element_by_css_selector("div[class = 'form-group'] input:nth-child(1)").click()
# x =[]
# x.index(2, 0)
# print(x)

import time

def procedure():
   time.sleep(2.5)

# measure process time
# t0 = time.clock()
# procedure()
# print(time.clock(), "seconds process time")

# measure wall time
t0 = time.time()
procedure()
print(time.time() - t0, "seconds wall time")
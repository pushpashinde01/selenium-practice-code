from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.youtube.com')

driver.find_element_by_xpath('//yt-icon[@class = "style-scope ytd-searchbox"]').click()
driver.find_element_by_name('search_query').send_keys('Sushant Ghadage')

# driver.implicitly_wait(10)
time.sleep(3)
driver.find_element_by_xpath('//yt-icon[@class = "style-scope ytd-searchbox"]').click()
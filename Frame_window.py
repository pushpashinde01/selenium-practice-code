from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame('mce_0_ifr')
driver.find_element_by_xpath('//body/p').clear()
driver.find_element_by_xpath('//body/p').send_keys('Entered text into frame now')

# to get out of frame and to get normal https u need to use below
driver.switch_to.default_content() # if we comment out this line then we will get an error
print(driver.find_element_by_xpath('//div/h3').text)

driver.close()
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/angularpractice')

driver.find_element_by_name('name').send_keys('pushpa')

# to get text that we eneter through selenium can get by get attribute

print(driver.find_element_by_name('name').get_attribute('value'))
# or you can use java script executer in selenium
# whihc is JS DOM(Java script Document Object Model)

print(driver.execute_script('return document.getElementsByName("name")[0].value'))

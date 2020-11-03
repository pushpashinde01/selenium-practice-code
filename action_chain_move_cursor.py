from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

# Check that displayed-text is display on page or not
print(driver.find_element_by_id('displayed-text').is_displayed(),'displaying')

driver.find_element_by_id('hide-textbox').click()
driver.implicitly_wait(5)
print(driver.find_element_by_id('displayed-text').is_displayed(),'displaying')
action = ActionChains(driver)
button = driver.find_element_by_id('mousehover')
action.move_to_element(button).perform()

# to click on top
link_button = driver.find_element_by_link_text('Top')
# action.move_to_element(link_button).click().perform()
link_button.click()

driver.implicitly_wait(10)

driver.get('https://chercher.tech/practice/practice-pop-ups-selenium-webdriver')
# double_click = driver.find_element_by_id('double-click')
# action = ActionChains(driver)
# action.move_to_element(double_click).double_click().perform()

# For clicking on alert as alert is not html so switch to alert
# alert = driver.switch_to.alert
# alert.accept()
# # alert.send_keys()
# driver.implicitly_wait(15)

# driver.switch_to.default_content()
prompt = driver.find_element_by_name('prompt').click()
alert = driver.switch_to.alert
alert.send_keys('entering text')

# alert.accept()
# driver.close()


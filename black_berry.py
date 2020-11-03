from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/angularpractice/')

driver.find_element_by_link_text('Shop').click()
driver.implicitly_wait(5)

black = driver.find_element_by_link_text('Blackberry')

black.find_element_by_xpath('parent::h4/parent::div/parent::div/div[@class = "card-footer"]/button').click()


driver.find_element_by_xpath("//ul/li/a[@class = 'nav-link btn btn-primary']").click()

driver.find_element_by_xpath("//button[@class = 'btn btn-success']").click()

# purchase page
driver.find_element_by_id("country").send_keys('ind')
# driver.implicitly_wait(7)
# impliment explicit wait
wait = WebDriverWait(driver,7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
# expected_conditions()

driver.find_element_by_link_text('India').click()
# suggestions = driver.find_elements_by_xpath("//div[@class = 'suggestions']/ul/li/a")
# for sugg in suggestions:
#     if sugg.text == 'India':
#         print("text is ",sugg.text)
#         sugg.click()

driver.find_element_by_xpath("//div/label[@for = 'checkbox2']").click()

driver.find_element_by_css_selector("input[class= 'btn btn-success btn-lg']").click()

text = (driver.find_element_by_class_name("alert-success").text)


assert 'Success!' in text

driver.get_screenshot_as_file('screen.png')

driver.quit()
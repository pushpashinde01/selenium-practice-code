from selenium import webdriver
driver = webdriver.Chrome(executable_path= './chromedriver.exe')

# '''project 1'''
#
driver.get('https://login.salesforce.com/')

''' by name'''
driver.find_element_by_id('username').send_keys('rahul')
driver.find_element_by_name('pw').send_keys('shetty')

driver.find_element_by_name('pw').clear()

driver.find_element_by_name('pw').send_keys('shetty123')

driver.find_element_by_id('rememberUn').click()

driver.find_element_by_id('Login').click()

# driver.find_element_by_link_text('Forgot Your Password?').click()
driver.find_element_by_id('forgot_password_link').click()
driver.find_element_by_link_text('Cancel').click()

# print(driver.find_element_by_id('chooser_error').text)
# print(driver.find_element_by_xpath('//div[@id="error"]').text)
# print(driver.find_element_by_class_name('loginError').text)

# driver.close()

# '''There is difference between find_element_by and find_elements_by'''
# '''css selector'''
# # driver.find_element_by_css_selector('#uasername').send_keys('rahul') #id
# # driver.find_element_by_css_selector('.uasername').send_keys('rahul') #.classname
# # op = driver.find_element_by_css_selector('input[id = "username"]')
# # op = driver.find_element_by_css_selector('input.username')
#
# ''' x path'''
# # driver.find_element_by_xpath('//input[@id = "username"]').send_keys('pushpa') #success
# # driver.find_element_by_xpath('//input[(@class="username"]').send_keys('pushpa)

# '''project 2'''
# driver.get('https://rahulshettyacademy.com/angularpractice')
# driver.find_element_by_name('name').send_keys('rahul')
# driver.find_element_by_name('email').send_keys('rahul@gmail.com')
#
#
# driver.find_element_by_xpath('//input[@type = "submit"]').click()
# print(driver.find_element_by_class_name('alert-success').text)

# driver.find_element_by_css_selector('input[name = "name"]').send_keys('rahul')


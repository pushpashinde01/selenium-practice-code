from selenium import webdriver

option = webdriver.ChromeOptions()
# option.add_argument('headless')
option.add_argument('--start-maximized')
option.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome("chromedriver.exe",options=option)
driver.get('https://rahulshettyacademy.com/angularpractice/')

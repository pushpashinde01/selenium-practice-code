from selenium import webdriver

# browser = webdriver.Chrome(executable_path='C:\\Users\\111205\\PycharmProjects\\selenium_project2\\chromedriver.exe')
browser = webdriver.Chrome('.\chromedriver.exe')
# browser = webdriver.Chrome()
print(browser)
browser.get('https://www.youtube.com')

search_box = browser.find_elements_by_xpath('//*[@id="search"]')
print(search_box)
search_box.send_keys('Al Sweigart')

search_button = browser.find_elements_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')
search_button.click()

browser.close()
browser.quit()
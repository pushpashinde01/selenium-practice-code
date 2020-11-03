from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text('Click Here').click()
# now child window get open to get that page you will need to do driver.get()
# so insteda of that use below

child_window = driver.window_handles[1]
driver.switch_to.window(child_window)
print(driver.find_element_by_tag_name('h3').text)

# if you want to go back to parent window just use below
driver.switch_to.window(driver.window_handles[0])
print(driver.find_element_by_tag_name('h3').text)
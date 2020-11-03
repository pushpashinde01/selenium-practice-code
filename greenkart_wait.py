from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

search_list = ['bro', 'cau','cap', 'cas']
product_check = ['Brocolli', 'Cauliflower','Capsicum', 'Cashews']
driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
searh_but = driver.find_element_by_xpath('//input[@type="search"]')
# driver.save_screenshot()
# driver.scree
list1 = []
for count in range(len(search_list)):
    searh_but.clear()
    searh_but.send_keys(search_list[count])
    time.sleep(2)
    # product_name = driver.find_element_by_xpath('//div[@class="product-image"]/img').get_attribute('src')
    product_name = driver.find_element_by_xpath('//div[@class="product"]/h4[@class = "product-name"]').text
    if search_list[count] in product_name.lower():
        driver.find_element_by_xpath('//div[@class ="product-action"]/button').click()
    list1.append(product_name)

print("product names before cart are as below",list1 )
cart_but = driver.find_element_by_xpath('//a[@class="cart-icon"]/img[@alt="Cart"]').click()
time.sleep(1)
# driver.implicitly_wait(5) #This is global wait

checkout = driver.find_element_by_xpath('//div[@class="action-block"]/button[text()="PROCEED TO CHECKOUT"]').click()
time.sleep(2)
list2 = []
at_cart = driver.find_elements_by_xpath('//td/p[@class="product-name"]')
for pro_name in at_cart:
    list2.append(pro_name.text)


# Find out total amount display in table and  crosscheck it with total display on page
# if there are morae tag names then we can get it by using index. eg td[5]
amounts = driver.find_elements_by_xpath("//tr/td[5]/p")

total = [int(amount.text) for amount in amounts]
print("sum of total amount in table as", sum(total))

total_amnt = driver.find_element_by_class_name("totAmt").text
print("Total amount display in page",total_amnt)


print("product names at cart are as below",list2 )
amnt_val_before = driver.find_element_by_xpath('//span[@class="discountAmt"]').text
print("amount value before promo code is",amnt_val_before)

promo_code = driver.find_element_by_xpath('//div[@class="promoWrapper"]/input[@class="promoCode"]').send_keys('rahulshettyacademy')
time.sleep(2)
apply_button = driver.find_element_by_xpath('//div[@class="promoWrapper"]/button[@class="promoBtn"]').click()

# driver.implicitly_wait(15)
time.sleep(5)
# amnt_val_after = driver.find_element_by_class_name('discountAmt').text
amnt_val_after = driver.find_element_by_xpath('//span[@class="discountAmt"]').text
print("amount value after promo code is",amnt_val_after)

wait = WebDriverWait(driver,5)
# use of wait until
# wait.until(expected_conditions.presence_of_element_located(By.CLASS_NAME, "PROMO-CODE"))

place_order_but = driver.find_element_by_xpath('//button[text() ="Place Order"]').click()

if(list1 == list2):
    print("name got in cart")
else:
    print("name not in list")

assert list1 == list2

# driver.close()
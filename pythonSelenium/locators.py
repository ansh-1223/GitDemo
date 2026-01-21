import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME,"email").send_keys("ansh@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("anshu")
driver.find_element(By.ID,"exampleCheck1").click()

# XPATH- //tagname[@attribute='value']
# when we have multiple elements with same tag name and value then we use the count for xpath
# CSS-   tagname[attribute='value'], #id is also a css selector, .classname
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("anshu")
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()

#static dropdown for this we wrap the element in select class only when select tag is there
dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
#dropdown.select_by_value()

driver.find_element(By.XPATH,"//input[@type='submit']").click()
message=driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("hello world")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()
time.sleep(50)
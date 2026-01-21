import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
#we can also locate element by link text,"a ie anchor tag is link"
driver.find_element(By.LINK_TEXT,"Forgot password?").click()

# PARENT TO CHILD TRAVERSAL IN XPATH WE USE "/"
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")

# for Parent ot child traversal in CSS we use space in place of / and use nth-child for elements instead of []
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("1234")
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("1234")

#driver.find_element(By.XPATH,"//button[@type='submit']").click()
#we can also select element in xpath by text of the element directly
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()


time.sleep(50)
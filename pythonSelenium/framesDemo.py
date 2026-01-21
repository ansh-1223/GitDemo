import time

from selenium.webdriver.common.by import By
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
#here the text box is in frames so we cannot edit it directly as it is embeded in the page
driver.switch_to.frame("singleframe")
driver.find_element(By.CSS_SELECTOR,"input[type='text']").clear()
driver.find_element(By.CSS_SELECTOR,"input[type='text']").send_keys("hello")
driver.switch_to.default_content()
print(driver.find_element(By.LINK_TEXT,"Single Iframe").text)#we cannot do this directly as driver scope is now in frames
time.sleep(500)
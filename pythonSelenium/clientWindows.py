
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.implicitly_wait(5)

driver.find_element(By.LINK_TEXT,"Click Here").click()
#we cannot switch to other window directly for that we use window_handled which stores all windows as list
windowsopened=driver.window_handles
driver.switch_to.window(windowsopened[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.close()
driver.switch_to.window(windowsopened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text
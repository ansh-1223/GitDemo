import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)

#ActionChains is used for hovering and other actions
action= ActionChains(driver)
#action.double_click()
#action.context_click() it is right click
#action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()#perform is necessary
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
time.sleep(500)
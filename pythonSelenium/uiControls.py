import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

radioButton=driver.find_elements(By.CSS_SELECTOR,".radioButton")
radioButton[2].click()
assert radioButton[2].is_selected()

assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()

#assert not is used as negation
assert not driver.find_element(By.ID,"displayed-text").is_displayed()

time.sleep(15)

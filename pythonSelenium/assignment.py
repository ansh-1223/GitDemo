import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
windowsopened=driver.window_handles
driver.switch_to.window(windowsopened[1])
email=driver.find_element(By.LINK_TEXT,"mentor@rahulshettyacademy.com").text
driver.switch_to.window(windowsopened[0])
driver.find_element(By.ID,"username").send_keys(email)
driver.find_element(By.ID,"password").send_keys("12345")
driver.find_element(By.ID,"signInBtn").click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"div[style='display: block;']")))
print(driver.find_element(By.CLASS_NAME,"alert-danger").text)
time.sleep(500)
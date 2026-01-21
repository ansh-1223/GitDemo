import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.implicitly_wait(5)
#5 seconds is max timeout,as soon as the elements are loaded it proceeds
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
#Here we are using find elements so it returns a list and we need to use sleep as as soon as list is returned it proceeds and initially it will be empty
results=driver.find_elements(By.XPATH,"//div[@class='products']/div")
count=len(results)
assert count > 0
print(count)
for result in results:
    result.find_element(By.XPATH,"  div/button").click() #this is chaining from parent to child

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

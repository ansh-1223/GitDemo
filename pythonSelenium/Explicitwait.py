import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expectedList=['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList=[]

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
    actualList.append(result.find_element(By.XPATH,"h4").text)
    result.find_element(By.XPATH,"  div/button").click() #this is chaining from parent to child
time.sleep(2)
assert actualList == expectedList
print(actualList)
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

#sum validation
prices=driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sumn=0
for price in prices:
    sumn=sumn+int(price.text)
print(sumn)
totalAmount=int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

#Explicit wait
#here we specify wait for specific elements
wait=WebDriverWait(driver,10) #10 sec is max timeout it can close as soon as its loaded
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

discamnt=float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
assert discamnt < totalAmount
time.sleep(500)
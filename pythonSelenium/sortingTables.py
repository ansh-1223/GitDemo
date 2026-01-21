from selenium import webdriver
from selenium.webdriver.common.by import By
browserSortedVegies=[]
driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
#here we get sorted elements from browser which we will comapre by manually sorting elements
#so that to confirm they are sorted or there is a bug
vegelements=driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in vegelements:
    browserSortedVegies.append(ele.text)

originalsortedlist=browserSortedVegies.copy()
browserSortedVegies.sort()
assert originalsortedlist==browserSortedVegies

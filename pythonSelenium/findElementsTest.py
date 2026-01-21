import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
#find elements finds all the matching elements on the page it returns list of web elements
countries= driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break

#print(driver.find_element(By.ID,"autosuggest").text)  This will not give India as .text only returns text which is inbuilt on the site not by automation
#this is dom attribute which stores the text everytime the value changes
assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"


time.sleep(500)
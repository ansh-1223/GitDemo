import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
#these two steps we manually download the chrome driver and import
#service_obj=Service("c/users/chromedriver")
#driver1=webdriver.Chrome(service=service_obj)

#when we call chrome then chrom driver service is called in backend chrome is downloaded on our behalf
driver=webdriver.Edge()
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(5)#we use this so that the browser dont close instantly and we can see the content
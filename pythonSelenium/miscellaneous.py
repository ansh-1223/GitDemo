import time

from selenium import webdriver

chrome_optons=webdriver.ChromeOptions()
#in headless mode browser dont open but tests are performed
chrome_optons.add_argument('headless')
#this ignores all errors while opening and move to website
chrome_optons.add_argument('--ignore-certificate-errors')
chrome_optons.add_argument('--no-sandbox')
driver=webdriver.Chrome(chrome_optons)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#execute script is used to execute javascript within selenium
#this is used for scrolling to the bottom
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#this takes screenshots
driver.get_screenshot_as_file("screen.png")
#time.sleep(5)
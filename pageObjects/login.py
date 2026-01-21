from selenium.webdriver.common.bidi.browser import Browser
from selenium.webdriver.common.by import By

from pageObjects.shop import ShopPage
from utils.browserUtils import BrowserUtils


#here we are attaching the parameter username_input to self so that we can use it anywhere in the class
#class(parentclass):
class LoginPage(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver) #here we initialize the parent class constructor
        self.driver = driver
        self.username_input=(By.ID, "username")
        self.password_input=(By.NAME, "password")
        self.signInBtn=(By.ID, "signInBtn")



    def login(self,username,password):
        #here * unpacks the locator as find element takes two inputs
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.signInBtn).click()
        shopPage = ShopPage(self.driver)
        return shopPage
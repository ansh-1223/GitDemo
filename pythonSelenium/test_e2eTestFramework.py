#here in function we can only pass fixtures
#when code runs it search for browser instance in the file and then it searches conftest for fxiture
#pytest xdist is the plugin we need to run the tests in parallel pytest -n number pf test to run
#pytest -n 2 -m smoke --browser_name edge --html reports/report.html
#jenkins username=anshuman pass Ansh@1234
import json
import os.path
import sys
import time

import pytest

#this adds the file to the systems path
#java -jar jenkins.war --httpPort=9090 to run jenkins
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.login import LoginPage
from pageObjects.shop import ShopPage
test_data_path='../data/test_e2eTestFramework.json'
with open(test_data_path) as f:
    test_data = json.load(f) #load converts json into python object
    test_list=test_data["data"]

#here parametrize accespts a list in terms of test_list and passes the  index in test_list_item for each iteration
@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):

    driver=browserInstance
    loginPage=LoginPage(driver)
    print(loginPage.getTitle())
    shopPage=loginPage.login(test_list_item["userEmail"],test_list_item["userPassword"])#this we can write as login method is returning shop page object
    shopPage.add_product_to_cart(test_list_item["productName"])
    print(shopPage.getTitle())
    checkout_confirmation=shopPage.go_to_cart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.validate_order()


    time.sleep(5)
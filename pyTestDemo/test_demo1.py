#any pytest file should start with test_ or end with _test
#all code should be inside a function for pytest
#pytest method name should start with test_
import pytest


#py.test command to run test from command prompt
#py.test -v to get more info
#py.test -v -s  s is used to print console logs
#we cannot have same method names in pytest

@pytest.mark.smoke
def test_firstGreet():
    print("hello world")

@pytest.mark.xfail
def test_secondGreetCreditCard():
    print("good morning")

#here we use the index of the tuple which data to be retrieved on every run
def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
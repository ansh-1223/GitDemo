#@pytest.fixture is used to tag the method which will run first before the test,it is generally for setups or opening a browser
#yield is used to run to do last things such as close the browser or clear cookies
#by wrapping the methods in class we can mark the class with usefixtures and pass the fixture which will apply to all methods
import pytest


@pytest.mark.usefixtures("setup")
class TestFix:

    def test_fixtureDemo(self):
        print("hello world")

    def test_fixtureDemo2(self):
        print("hello world")

    def test_fixtureDemo3(self):
        print("hello world")
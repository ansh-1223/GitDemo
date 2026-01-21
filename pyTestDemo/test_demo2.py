#to test a single program from command line we give file name infront of py.test <filename>
#we should have specific meaningful name for the methods
#to run specific test cases we do grouping by regular expression when the cases have a common name present
#py.test -k CreditCard -v -s it run only the cases with creditcard in the method name
#-k for method name execution
#you can mark(tag) tests with @pytest.mark.smoke and then run them with -m
#you can skip tests with @pytest.mark.skip
#@pytest.mark.xfail this is used to run the test but not reprt it


import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_FirstProgram():
    msg="Hello"
    assert msg == "Hi", "test failed"

def test_secondCreditCard():
    a=2
    b=3
    assert a+b == 5, "test failed"

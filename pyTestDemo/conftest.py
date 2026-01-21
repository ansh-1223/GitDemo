#conftest file is common file available to all the files
#you can use this when a fixture needs to be used by all tests
#scope is used to define around which the test will run
#here we have data setup in a fixture which we return as a tuple which can be used by other tests
#WE use params to run the test number of times the params ie if 3 params it runs 3 time and request keyword is needed to be used
#data driven and paramaterization is done using tuples and return statement
import pytest


@pytest.fixture(scope="class")
def setup():
    print("i will run first")
    yield
    print("i will run last")

#DATA DRIVEN
@pytest.fixture()
def dataLoad():
    print("user profile is being created")
    return ["Anshu","Singh","hello@gmail.com"]

#PARAMATERIZATIION OF FIXTURES
#here we can run our tests by a dataset
#params is used to pass the data set and request.param return each date one by one so it runs 3 times
#to send multipe values in a single run we wrap in brackets
@pytest.fixture(params=[("chrome","anshu"),("firefox","new"),("IE","SS")])
def crossBrowser(request):
    return request.param
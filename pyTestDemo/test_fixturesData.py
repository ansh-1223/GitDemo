#though we are declaring the fixture globally we have to pass the fixture in method as an argument when it has to return
#some data

import pytest



@pytest.mark.usefixtures("dataLoad")
class TestExample2:
    def test_editProfile(self,dataLoad):
        print(dataLoad[0])
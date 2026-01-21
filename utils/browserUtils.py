#when we have common code then we create utility files which we can reuse by passing them as parent

class BrowserUtils:

    def __init__(self,driver):
        self.driver=driver

    def getTitle(self):
        return self.driver.title
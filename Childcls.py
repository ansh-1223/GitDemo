from Classes import Calculator


class ChildImpl(Calculator):
    num2=100

    def __init__(self):
        Calculator.__init__(self,2,10) # we need to call parent constructor in child constructor when constructor is not default and it has some code in it
    def getCompleteData(self):
        return self.num2+self.num+self.sumation()

obj=ChildImpl()
print(obj.getCompleteData())

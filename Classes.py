#class
#when we create a class a default constructor is already there when creating object
#self keyword is mandatory for calling variable name in methods
#constructor name should be __init__
#instance variale is linked to objects

class Calculator:
    num=1
    #default constructor
    def __init__(self,a,b): # a and b are instance variable as they are created everytime object is created
        self.firstnumber=a
        self.secondnumber=b
        print("I am called automatically when creating a object")

    def getData(self): #methods are same as functions inside a class
        print("Executing a method in the class")
    def sumation(self):
        return self.firstnumber+self.secondnumber+Calculator.num #we cannot call variable independently in methods,always need to use .

obj=Calculator(2,3) #syntax to create objects in python
obj.getData()
print(obj.sumation())
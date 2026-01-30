class Arithmetic:
    def __init__(self):   #Consttructor
        self.Value1=0
        self.Value2=0

    def Accept(self):  #Instance method
        No1=int(input("Enter first number : "))
        No2=int(input("Enter first number : "))

        self.Value1=No1
        self.Value2=No2

    def Addition(self):
        print("The addition of two numbers is : ",self.Value1 + self.Value2)

    def Subtraction(self):
        print("The Subtraction of two numbers is : ",self.Value1 - self.Value2)

    def Multiplication(self):
        print("The Multiplication of two numbers is : ",self.Value1 * self.Value2)

    def Division(self):
        try :
            self.Div=self.Value1 / self.Value2
            print("The Division of two numbers is : ",self.Div)
        except ZeroDivisionError:
            print("Unable to divide by zero")

    
obj1=Arithmetic()
obj2=Arithmetic()
obj3=Arithmetic()

obj1.Accept()
obj1.Addition()
obj1.Subtraction()
obj1.Multiplication()
obj1.Division()
print("-"*15)
obj2.Accept()
obj2.Addition()
obj2.Subtraction()
obj2.Multiplication()
obj2.Division()
print("-"*15)
obj3.Accept()
obj3.Addition()
obj3.Subtraction()
obj3.Multiplication()
obj3.Division()
    

class Circle:
    #Class Var
    Pi=3.14

    def __init__(self):
        self.R=0.0
        self.A=0.0
        self.C=0.0

    def Accept(self):
        Radius=int(input("Enter the radius : "))
        self.R=Radius
        

    def CalculateArea(self):
        Area=self.R * self.R * Circle.Pi 
        self.A=Area

    def CalculateCircumference(self):
        Circumference=self.R * 2 * Circle.Pi
        self.C=Circumference

    def Display(self):
        print("The value of Radius is : ",self.R)
        print("The Area is : ",self.A)
        print("The Circumference is : ",self.C)


obj1=Circle()
obj2=Circle()
obj3=Circle()

obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()
print("-"*15)
obj2.Accept()
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()
print("-"*15)
obj3.Accept()
obj3.CalculateArea()
obj3.CalculateCircumference()
obj3.Display()




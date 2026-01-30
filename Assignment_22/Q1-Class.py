class Demo:
    value=10   #Class variable

    def __init__(self,A,B):
        self.no1=A
        self.no2=B
        print("Inside constructor")

    def fun(self):
        print("Inside fun instance behaviour : ",self.no1)
        print("Inside fun instance behaviour : ",self.no2)

    def gun(self):
        print("Inside gun instance behaviour : ",self.no1)
        print("Inside gun instance behaviour : ",self.no2)

obj1=Demo(11,21)
obj2=Demo(12,22)
print("-"*15)
obj1.fun()
print("-"*15)
obj1.gun()
print("-"*15)
obj2.fun()
print("-"*15)
obj2.gun()
        
        

        

    
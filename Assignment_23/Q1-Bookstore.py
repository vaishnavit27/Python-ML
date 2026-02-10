# ***

class Bookstore:
    NoofBooks=0

    def __init__(self,Name,Author):    #instannce method
        self.Name=Name
        self.Author=Author
        Bookstore.NoofBooks=Bookstore.NoofBooks+1

    def Display(self):    #instnace method
        print(f"{self.Name} by {self.Author}.No of Books is : {self.NoofBooks}")


obj1=Bookstore("Meluha","Amish")
obj1.Display()

obj2=Bookstore("Alchemist","Paulo")
obj2.Display()


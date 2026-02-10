class BankAccount:
    ROI = 10.5

    def __init__(self,Name,Amount):
        self.Name=Name
        self.Amount=Amount

    def Display(self):
        print("Name of Acc holder is : ",self.Name)
        print("Current Balance of Acc Holder is : ",self.Amount)


    def Deposit(self,):
        try:
            A=int(input("Enter Amount to be Added : "))
            self.Amount=self.Amount+A
            print(f"{A} amount Deposited. Current Balance after Deposit is {self.Amount}")

        except ValueError:
            print("Enter proper Value")



        

    
    def WithDraw(self):
        try:
            W=int(input("Enter amount to be Withdrawed : "))
            if self.Amount > W:

                self.Amount = self.Amount - W
                print(f"{W} amount withdrawed. Current Balance after withdrawal is {self.Amount}")

            else:
                print("No Sufficient Balance Available")

        except ValueError:
            print("Enter proper value")

        

    
    def CalculateInterest(self):

        self.Interest = (self.Amount * self.ROI) / 100
        print(f"The Total Amount after ROI is : {self.Interest}")


obj1=BankAccount("Vaishnavi",75000)
obj1.Display()
obj1.Deposit()
obj1.WithDraw()
obj1.CalculateInterest()

print("-"*50)

obj2=BankAccount("Hemchandra",90000)
obj2.Display()
obj2.Deposit()
obj2.WithDraw()
obj2.CalculateInterest()

print("-"*50)

obj3=BankAccount("Prathmesh",85000)
obj3.Display()
obj3.Deposit()
obj3.WithDraw()
obj3.CalculateInterest()


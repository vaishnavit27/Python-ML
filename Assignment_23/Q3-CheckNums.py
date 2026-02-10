class Numbers:
    def __init__(self):
        self.value = int(input("Enter a number : "))

    def ChkPrime(self):
        
        count=0
        for i in range(1,self.value+1):
            if self.value % i == 0 :
                count = count + 1 
         
        if count > 2 :
            return False
        else:
            return True


            
    def ChkPerfect(self):
        if self.value < 1:
            return False
        self.perfectsum = 0
        for i in range(1, self.value):
            if self.value % i == 0:
                self.perfectsum += i
        return self.perfectsum == self.value

    def Factors(self):
        for i in range(1,self.value):
            if self.value%i==0:
                print(i,end = " ")
                
            else:
                pass

    def SumFactors(self):
        Sum=0
        for i in range(1,self.value):
            if self.value%i==0:
                Sum=Sum+i
               
                
            else:
                pass
        return Sum
        


for _ in range(3):
    obj = Numbers()
    print("Prime:", obj.ChkPrime())
    print("Perfect:", obj.ChkPerfect())
    obj.Factors()
    print("\n")
    print("SumFactors : ",obj.SumFactors())
    print("\n")
    print("-" * 50)



            


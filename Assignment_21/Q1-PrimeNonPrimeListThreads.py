
import threading


def Prime(Data):


    # Factors = []    ->   Wrong
    Final = []
    
    # Find Factors of No
    for i in Data:

        Factors = []      # to get factors list for every element in Data
        for num in range(1,i+1):
            if i % num == 0:
                Factors.append(num)
        if len(Factors) == 2:
                Final.append(i)   


    print("Prime Elements from list are : ",Final)


def NonPrime(Data):
     
    Final = []

    for i in Data : 
          
        factors = []

        for num in range(1,i+1):
            if i % num == 0 :
                factors.append(num)

        if len(factors) > 2 :
            Final.append(i)

    print("NonPrime Elements from list are : ",Final)

        
            

if __name__ == "__main__":

    Size = 0

    print("Enter the number of elements : ")
    Size = int(input())

    Data = []

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread(target= Prime , args= (Data,) , name = "PrimeThread")
    t2 = threading.Thread(target= NonPrime , args= (Data,) , name = "NonPrimeThread")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")



import threading

def SumEvenFactor(No):

    
    
    sumE = 0

    for i in range(1,No+1):
        if No%i == 0:
            if i%2 == 0 :
                sumE = sumE + i 

    print(f"Sum of Even Factors of number {No} is {sumE}")


def SumOddFactor(No):

    
    
    sumO = 0

    for i in range(1,No+1):
        if No%i == 0:
            if i%2 != 0 :
                sumO = sumO + i 

    print(f"Sum of Odd Factors of number {No} is {sumO}")




if __name__ == "__main__":

    t1 = threading.Thread(target = SumEvenFactor, args = (12,), name = "SumEvenFactorthread")
    t2 = threading.Thread(target = SumOddFactor, args = (12,), name = "SumOddFactorthread")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")
import threading

def EvenList(Data):
    EvenData = list()
    Sum = 0
    for i in Data : 
        if i % 2 == 0 :
            EvenData.append(i)
            Sum = Sum + i

    print("The EvenList is : ")
    print(EvenData)
    print(f"The Sum of data in Even list is : {Sum}")


def OddList(Data):
    OddData = list()
    Sum = 0
    for i in Data : 
        if i % 2 != 0 :
            OddData.append(i)
            Sum =  Sum + i

    print("The OddList is : ")
    print(OddData)
    print(f"The Sum of data in Odd list is : {Sum}")



if __name__ == "__main__":

    value = 0 
    Size = 0

    print("Enter the number of Elements : ")
    Size  = int(input())
    print(f"The size of the elements is : {Size}")

    Data = list()

    for i in range(Size):
        value = int(input("Enter Elements : "))
        Data.append(value)
        
    print("The elements in the list are : ")
    print(Data)

    t1 = threading.Thread(target= EvenList,args= (Data,),name = "EvenListThread")
    t2 = threading.Thread(target= OddList,args= (Data,),name = "OddListThread")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")




    
    

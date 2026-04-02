import threading

def Max(Data):

    max_value = Data[0]

    for i in Data:
        if i > max_value :
            max_value = i

    print("Max value of the Elements is : ",max_value)


def Min(Data):

    min_value = Data[0]

    for i in Data:
        if i < min_value :
            min_value = i

    print("Min value of the Elements is : ",min_value)



if __name__ == "__main__":

    Size = 0

    print("Enter the number of elements : ")
    Size = int(input())

    Data = []

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread(target= Max , args= (Data,) , name = "MaxThread")
    t2 = threading.Thread(target= Min , args= (Data,) , name = "MinThread")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")
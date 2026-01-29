def Min(Data):    #Procedural Programming  #user defined min function
    print(Data)
    min_value=Data[0]
    for i in Data:
        if i<min_value:
            min_value=i
    return min_value
        


def main():
    No=int(input("Number of Elements : "))

    Value=0

    Data=list()

    for i in range(No):
        Value=int(input("Enter Elements : "))
        Data.append(Value)

    Ret=0
    Ret=Min(Data)
    print("The minimum of elements is : ",Ret)



if __name__ == "__main__":
    main()
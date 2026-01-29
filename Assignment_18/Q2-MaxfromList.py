def Max(Data):    # User defined max function
    max_value=Data[0]
    for i in Data:
        if i>max_value:
            max_value=i

    return max_value
    



def main():
    No=int(input("Enter number of elements : "))

    Value=0

    Data=list()
    
    for i in range(No):
        Value= (int(input("Enter Element : ")))
        Data.append(Value)

    ret=Max(Data)
    print(ret)

    

if __name__ == "__main__":
    main()
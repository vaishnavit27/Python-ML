def sum(Data):
    sum=0
    for i in range(len(Data)):
        sum=sum+Data[i]
    return sum
    

    
    



def main():
    No=0
    Value=0
    

    No=int(input("Number of Elements : "))
    
    Data=list()
    print("Enter the elements (followed with enter at every element): ")
    
    for i in range(No):
        Value=int(input())
        Data.append(Value)

    Ret=0
    Ret=sum(Data)
    print("The Sum of all the elements in a list : ",Ret)
    



if __name__ == "__main__":
    main()

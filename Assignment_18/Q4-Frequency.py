
def main():
    No=int(input("Number of elements : "))
    value=0
    Ret=0

    Data=list()

    for i in range(No):
        value=int(input("Enter elements : "))
        Data.append(value)

    print(Data)

    Num=int(input("Enter a number to check frequency : "))
    count=0
    
    for i in Data:     # i=0 = value 1 in list ,i=1 = value 2 in list
        if Num==i:
            count=count+1
        
        
    print(count)


if __name__ == "__main__":
    main()

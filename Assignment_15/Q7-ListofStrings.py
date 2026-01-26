#***

def main():
    Data=list()
    Data=input("Enter List of Strings : ")
    print("The actual list of strings is : ",Data)
    listofData=Data.split()
    print("The list of Data is : ",listofData)

    for i in listofData:
        
        length= len(i)
    print("The length of the string is : ",length,end=" ")

    

    FData=list(filter(lambda data :len(data) >5,listofData))
    print("\nThe filtered Data is : ",FData)    

if __name__ == "__main__":
    main()


# def length(ListofData):
#     length=len(ListofData)
#     if length>5:
#         print(ListofData)
    
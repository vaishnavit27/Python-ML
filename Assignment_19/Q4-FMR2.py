from functools import reduce
 

def main():
    No=0
    value=0
    Data=list()
    Ret=0

    No=int(input("Number of elements : "))

    print("Enter Elements (Followed by a enter after every element) : ")

    for i in range(No):
        value=int(input())
        Data.append(value)

    print("Input list : ",Data)

    FData=list(filter((lambda No : (No%2==0) ),Data))
    print("Filtered Data is : ",FData)

    MData=list(map((lambda No : No**2 ),FData))
    print("Data after mapping is : ",MData)

    RData=reduce((lambda A,B:A+B),MData)
    print("Reduced Data is : ",RData)





if __name__=="__main__":
    main()

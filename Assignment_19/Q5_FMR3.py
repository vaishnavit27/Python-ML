from functools import reduce
 
def is_prime(n):
    for i in range(2,n):
        if n%i != 0:
            return True
        else:
            return False
        
        
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

    

    FData=list(filter(is_prime,Data))
    print("Filtered Data is : ",FData)

    MData=list(map((lambda No : No*2 ),FData))
    print("Data after mapping is : ",MData)

    RData=reduce((lambda A,B:A if A>B else B),MData)
    print("Reduced Data is : ",RData)





if __name__=="__main__":
    main()

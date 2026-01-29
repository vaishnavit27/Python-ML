def Sumdig(No):
    sum=0
    while(No>0):
        value=No%10   #gives remainder
        sum=sum+value
        No=No//10  #gives quotient

    return sum

def main():
    No=int(input("Enter a number : "))
    Ret=Sumdig(No)
    print(Ret)

if __name__ == "__main__":
    main()
        
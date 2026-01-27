def Add(A,B):
    return A+B

def main():
    No1=int(input("Enter first number : "))
    No2=int(input("Enter second number : "))

    Ret=Add(No1,No2)

    print(f"The Result of the two numbers {No1} {No2} is {Ret}")


if __name__=="__main__":
    main()
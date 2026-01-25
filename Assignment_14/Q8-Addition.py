Add = lambda A,B : (A+B)

def main():
    A=0
    B=0
    Sum=0

    A=int(input("Enter first number : "))
    B=int(input("Enter second number : "))

    Sum=Add(A,B)

    print("The addition is : ",Sum)

if __name__ == "__main__":
    main()
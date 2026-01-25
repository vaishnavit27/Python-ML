Mul= lambda A,B : (A*B)

def main():
    A=0
    B=0
    Res=0

    A=int(input("Enter first number : "))
    B=int(input("Enter second number : "))

    Res=Mul(A,B)

    print("The multiplication is : ",Res)

if __name__ == "__main__":
    main()
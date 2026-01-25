Largest = lambda A,B,C : (A,B,C)


def main():
    A=0
    B=0
    C=0
    Res=False
    
    A=int(input("Enter first number : "))
    B=int(input("Enter second number : "))
    C=int(input("Enter third number : "))
    Res=Largest(A,B,C)

    if (A>B and A>C ):
        print("The Largest number is : ",A)
    elif(B>A and B>C):
        print("The Largest number is : ",B)
    else:
        print("The Largest number is : ",C)






if __name__ == "__main__":
    main()
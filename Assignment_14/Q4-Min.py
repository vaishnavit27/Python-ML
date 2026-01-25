Minnum=lambda A,B:(A>B)

def main():
    A=0
    B=0
    Res=False
    

    A=int(input("Enter first number : "))
    B=int(input("Enter second number : "))
    Res=Minnum(A,B)

    if Res==True:
        print(B)
    else:
        print(A)


if __name__ == "__main__":
    main()
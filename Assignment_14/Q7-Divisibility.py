CheckDivisibility = lambda No : (No%5==0)


def main():
    No=0
    Res=False

    No=int(input("Enter a number : "))
    Res=CheckDivisibility(No)

    if (Res==True):
        print("True")

    else:
        print("False")

if __name__ == "__main__":
    main()
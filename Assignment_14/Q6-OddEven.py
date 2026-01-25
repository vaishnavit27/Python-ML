CheckEvenOdd = lambda No : (No%2==0)


def main():
    No=0
    Res=False

    No=int(input("Enter a number : "))
    Res=CheckEvenOdd(No)

    if (Res==True):
        return False

    else:
        return True

if __name__ == "__main__":
    Res=main()
    print(Res)
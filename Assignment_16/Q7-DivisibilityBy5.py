def CheckDivisibility(No):
    if No%5==0:
        return True
    else:
        return False

def main():
    No=int(input("Enter a number : "))
    Ret=CheckDivisibility(No)
    print(Ret)

if __name__ == "__main__":
    main()
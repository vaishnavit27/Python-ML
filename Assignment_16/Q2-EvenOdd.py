def CheckNum(No):
    if No%2==0:
        return "Even"
    else:
        return "Odd"

def main():
    No=int(input("Enter a number : "))
    Ret=CheckNum(No)
    print(Ret)

if __name__ == "__main__":
    main()
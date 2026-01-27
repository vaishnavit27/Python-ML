def CheckNum(No):
    if No>0:
        return "Positive Number"
    elif No<0:
        return "Negative Number"
    else:
        return "Zero"
    
def main():
    No=int(input("Enter a number : "))
    Ret=CheckNum(No)
    print(Ret)

if __name__ == "__main__":
    main()
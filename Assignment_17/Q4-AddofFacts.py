def Addfact(No):
    fact=1
    Sum=0
    for i in range(1,No+1):
        fact=fact*i
        Sum=Sum+fact
    return Sum

def main():
    No=int(input("Enter a number : "))
    Ret=Addfact(No)
    print(f"The Sum of factorial of {No} is {Ret}")

if __name__ == "__main__":
    main()
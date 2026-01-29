def CheckPrime(No):
    for i in range(2,No):
        if No%i != 0:
            return "Prime Number"
        else:
            return "Not a prime number "

def main():
    No=int(input("Enter a number : "))
    Ret=CheckPrime(No)
    print(Ret)

if __name__ == "__main__":
    main()
        
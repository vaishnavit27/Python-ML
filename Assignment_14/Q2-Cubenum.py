Cubenum=lambda No:No**3

def main():
    No=int(input("Enter a number: "))
    Res=Cubenum(No)
    print(f"The cube of {No} is {Res}")

if __name__ == "__main__":
    main()
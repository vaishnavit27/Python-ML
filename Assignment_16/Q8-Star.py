def star(No):
    for i in range(No):
        print("*",end=" ")

def main():
    No=int(input("Enter a number : "))
    star(No)
    

if __name__ == "__main__":
    main()
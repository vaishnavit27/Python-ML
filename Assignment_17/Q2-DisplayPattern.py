def main():
    No=int(input("Enter a number : "))
    Display(No)


def Display(No):
    for i in range(No):
        
        print("*"*No)

if __name__=="__main__":
    main()
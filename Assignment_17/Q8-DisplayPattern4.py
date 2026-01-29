def Pattern(No):
    for j in range(1,No+1):   #Outer loop : Rows Specific
        for i in range(1,j+1):
            print(i,end=" ")
            
        print()



def main():
    No=int(input("Enter a number : "))
    Pattern(No)

if __name__ == "__main__":
    main()
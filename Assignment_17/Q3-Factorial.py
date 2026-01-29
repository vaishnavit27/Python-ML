def Fact(No):
    fact=1
    for i in range(1,No+1):
        
        
           # Ans = 5*4*3*2*1
        fact=fact*i

    return fact
    
def main():
    No=int(input("Enter a number : "))
    Ret=Fact(No)
    print(f"The Factorial of {No} is {Ret}")


if __name__=="__main__":
    main()
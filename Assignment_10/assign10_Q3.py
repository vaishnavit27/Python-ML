def Factorial(No):
    Fact=1
    for i in range(1,No+1):
        
        Fact=Fact*i
        
    
    print(f"The Factorial of {No} number is : {Fact}")
    
No=int(input("Enter a number : "))    
Factorial(No)


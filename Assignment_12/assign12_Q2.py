def factors(No):
    for i in range(1,No+1):
        if No%i==0:
            print(i,end=" ")
        
        
No=int(input("Enter a number : "))
factors(No)

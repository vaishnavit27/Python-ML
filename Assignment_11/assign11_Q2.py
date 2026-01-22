def countdigits(No):
    count=0
    while No>=0:
        count=count+1
        No=No//10   
        
    return count
        

No=int(input("Enter a number: "))
Res=countdigits(No)
print(f"The digit count for the number {No} is {Res}")
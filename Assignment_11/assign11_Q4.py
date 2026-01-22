def revdig(No):
    revdigit=0
    while No>0:
        digit=No%10
        revdigit=revdigit*10+digit
        
        No//=10
    return revdigit

No=int(input("Enter a number: "))
Res=revdig(No)
print(f"The Reverse of the number {No} is {Res}")
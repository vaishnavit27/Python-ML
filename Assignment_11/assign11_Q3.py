def sumofdig(No):
    sum=0
    while No>0:
        digit=No%10  #Get the last digit
        sum=sum+digit
        No//=10  #Removes the last digit
    return sum

No=int(input("Enter a number: "))
Res=sumofdig(No)
print(f"The sum of the number {No} is {Res}")
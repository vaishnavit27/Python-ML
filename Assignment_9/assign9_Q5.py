def Divisibility(No):
    if No%3==0 and No%5==0:
        print(f"{No} is Divisible by 3 and 5")
    else:
        print(f"{No} is not Divisible by 3 and 5")
    
No=int(input("Enter a number to check the divisibility by 3 and 5 : "))
Divisibility(No)
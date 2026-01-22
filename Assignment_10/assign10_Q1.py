def multable(No):
    for i in range(1,11):
        Ans=No*i
        print(f"{No} * {i} = {Ans}")
    
No=int(input("Enter a number for multiplication table : "))

multable(No)



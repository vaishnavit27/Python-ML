def binaryofnum(No):
    binary=""     #string format
    while No>0:
        num=No%2
        binary=str(num)+binary    #prepend the num and converted num to string for concatenation
        No=No//2

    print(binary)

No=int(input("Enter a number : "))
binaryofnum(No)

Num=int(input("enter a number to check correct binary repres: "))
print(bin(Num)[2:])
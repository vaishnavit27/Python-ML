def displayonlyodd(No):
    for i in range(No+1):
        if i%2!=0:
            print(i)

No=int(input("Enter a number:"))
displayonlyodd(No)

print("-"*15)

def display(No):
    for i in range(1,No+1,2):
        print(i)

No=int(input("Enter a number:"))
display(No)

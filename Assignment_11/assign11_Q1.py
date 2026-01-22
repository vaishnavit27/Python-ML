def checkprime(No):
    if No>=1:
        for i in range(2,No):
            if No%i==0:
                return False
            else:
                return True
    


No=int(input("Enter a number:"))
checkprime(No)

if checkprime(No)==True:
    print("Prime Number")
else:
    print("Not a Prime Number")    
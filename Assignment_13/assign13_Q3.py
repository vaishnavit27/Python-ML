def perfectnum(No):
    originalnum=No
    Sum=0
    for i in range(1,No+1):
        if No%i==0:
            Sum=Sum+i
            if originalnum==Sum:
                return "Perfect Number"
            else:
                return "Not a Perfect Number"
            
No=int(input("Enter a number to check perfect number : "))
Res=perfectnum(No)
print(Res)


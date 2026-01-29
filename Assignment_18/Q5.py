from MarvellousNum import CheckPrime

def ListPrime(Data):
    Sum=0
    prime_nums=[]
    for i in Data:
        Res=CheckPrime(i)
        if Res==True:
            Sum=Sum+i
            prime_nums.append(i)
    print(f"{Sum} , {prime_nums}")
    


def main():
    No=int(input("Number of Elements : "))
    value=0
    

    Data=list()

    for i in range(No):
        value=int(input("Enter elements : "))
        Data.append(value)

    ListPrime(Data)
    



if __name__ == "__main__":
    main()



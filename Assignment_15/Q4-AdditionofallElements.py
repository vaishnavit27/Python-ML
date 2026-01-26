from functools import reduce



def main():
    Data=[1,2,3,4,5,6,7,8,9]
    print("The actual Data is : ",Data)

    RData=reduce((lambda A,B : A+B),Data)
    print("The Data after reduce is : ",RData)


if __name__ == "__main__":
    main()
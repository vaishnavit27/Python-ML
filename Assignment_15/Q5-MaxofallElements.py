from functools import reduce

def main():
    Data=[11,21,32,45,67,34,25]
    print("The actual Data is : ",Data)

    RData=reduce((lambda A,B : A if A>B else B ),Data)
    print("The reduced data is : ",RData)


if __name__ == "__main__":
    main()
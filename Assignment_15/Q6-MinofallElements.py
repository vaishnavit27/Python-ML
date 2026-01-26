from functools import reduce
def main():
    Data=[12,32,43,10,43,56]
    print("The actual Data is : ",Data)

    RData=reduce((lambda A,B: A if A<B else B),Data)
    print("RData is : ",RData)


if __name__ == "__main__":
    main() 
from functools import reduce

def main():
    Data=[2,3,5,7,8]
    print("The Actual Data is : ",Data)

    R_Product=reduce((lambda A,B : A*B ),Data)
    print(R_Product)


if __name__ == "__main__":
    main()



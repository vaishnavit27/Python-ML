#dIVISIBILITY BY BOTH 3 AND 5

def main():
    Data=[1,2,3,4,5,6,15,20,9,8]
    print("The Actual Data is : ",Data)

    FData=list(filter((lambda No : No%3==0 and No%5==0 ),Data))
    print("The filtered data is : ",FData)



if __name__ == "__main__":
    main()
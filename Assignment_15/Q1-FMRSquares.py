#Functional Programming FMR lambda 
def main():
    Data=[2,3,4,5,6]
    print("The actual Data is : ",Data)

    MData=list(map((lambda No:No**2),Data))
    print("Data After map is : ",MData)

if __name__ == "__main__":
    main()

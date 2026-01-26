from functools import reduce

def main():
    Data=[1,2,3,4,5,6,7,10,23,56,74]
    print("The actual Data is : ",Data)

    FData=len(list(filter((lambda No : No % 2 == 0),Data)))
    print("The filtered Data is : ",FData)

    

    # Count=len(FData)
    # print(Count)

   
    


if __name__ == "__main__":
    main()






CheckOdd=lambda No : No%2==0

def FilterX(Task,Elements):
    Result=list()

    for no in Elements:
        Ret=Task(no)
        if Ret==False:
            Result.append(no)
    return Result


def main():
    Data=[1,2,3,4,5,6,7,8,9,10]
    print("The Actual Data is ",Data)

    FData=list(FilterX(CheckOdd,Data))
    print("FData is : ",FData)


if __name__ == "__main__":
    main()
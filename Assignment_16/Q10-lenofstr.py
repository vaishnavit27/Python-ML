def length(str):
    # Ret=len(str)
    # print(Ret)
    count=0
    for i in str:
        count=count+1
    print(count)

def main():
    str=input("Enter a name : ")
    length(str)

if __name__ == "__main__":
    main()
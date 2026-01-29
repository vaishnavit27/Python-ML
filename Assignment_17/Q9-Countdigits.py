def count(No):
    count=0
    
    while No>0:
        count=count+1
        No=No//10
    return count

def main():
    No=int(input("Enter a number : "))
    Ret=count(No)
    print(Ret)

if __name__ == "__main__":
    main()



#***

def Even():
    count=1
    i=1
    while(count<11):
        
        if i%2==0:
            print(i,end=" ")
            count+=1
        i=i+1           

def main():
    Even()

if __name__ == "__main__":
    main()
        

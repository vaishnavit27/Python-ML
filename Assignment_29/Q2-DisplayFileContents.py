import os




def main():
    FileName = input("Enter File Name : ")

    Res = os.path.exists(FileName)

    if Res==True:
        fobj = open(FileName,"r")
        print(fobj.read())
 

    else:
        print("There is no such file ")


if __name__ == "__main__":
    main()
    
    
        
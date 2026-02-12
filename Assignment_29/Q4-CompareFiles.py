import hashlib
import sys

def CheckSum(FileName1,FileName2):
    fobj = open(FileName1,"rb")
    fobj2=open(FileName2,"rb")

    hobj = hashlib.md5()
    hobj2 = hashlib.md5()

    Buffer1 = fobj.read(1000)
    Buffer2 = fobj2.read(1000)

    while(len(Buffer1)>0):
        hobj.update(Buffer1)
        Buffer1=fobj.read(1000)

    while(len(Buffer2)>0):
        hobj2.update(Buffer2)
        Buffer2 = fobj.read(1000)
        

    fobj.close()
    fobj2.close()

    if hobj.hexdigest() == hobj2.hexdigest():
        return "SUCCESS "
    else:
        return "FAILURE"



def main():
    FileName1 = sys.argv[1]
    FileName2 = sys.argv[2]
    print("FileName1 :",FileName1)
    print("FileName2 :",FileName2)

    Ret = CheckSum(FileName1,FileName2)
    print(Ret)

    



if __name__ == "__main__":
    main()

import sys
import os


def ChkFreq(FileName,String):

    fobj = open(FileName,"r")

    Data = fobj.read()

    Ret = Data.count(String)

    print(Ret)
     
   
def main():

    if len(sys.argv) < 3 :
        print("Usage: python ScriptName.py FileName String")
        return
    

    FileName = sys.argv[1]
    String = sys.argv[2]

    print("File Name is : ",FileName)
    print("String is : ",String)

    

    ChkFreq(FileName,String)



if __name__ == "__main__":
    main()
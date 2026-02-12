import os
import sys
import shutil

def Copy(sourcefile,dest_file):
    shutil.copy2(sourcefile,dest_file)

    dobj= open(dest_file,"r")
    print("Contents Copied to new file are : ",dobj.read())

    
    


def main():

    FileName = sys.argv[1]
    print("FileName : ",FileName)

    fobj = open(FileName,"r")
    print("File Contents : ",fobj.read())

    FileName2="ABC.txt"

    # Ret= os.path.exists(FileName2)
    # if Ret==True:
    #     print("File Exists")
    # else:
    #     print("Have to create new File")

    hobj=open(FileName2,"w")
    print("New File Created : ",FileName2)

    Copy(FileName,FileName2)

    



if __name__ == "__main__":
    main()



    











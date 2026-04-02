import threading

def Small(String):

    print(f"Thread Name : {threading.current_thread().name} and Thread ID is : {threading.get_ident()} ")

    count = 0
    for char in String : 
        
        if char.islower():
            count = count+1
    print("The total number of lowercase characters in entered string is  : ",count)
    print("-"*35)
    

    
def Capital(String):

    print(f"Thread Name : {threading.current_thread().name} and Thread ID is : {threading.get_ident()} "
          )
    count = 0
    for char in String : 
        if char.isupper():
            count = count+1
    print("The total number of uppercase characters in entered string is  : ",count)
    print("-"*35)



def Digits(String):

    print(f"Thread Name : {threading.current_thread().name} and Thread ID is : {threading.get_ident()} ")

    count = 0
    for char in String:
        if char.isdigit():
            count = count + 1

    print("The total number of digits in entered string is  : ",count)
    print("-"*35)





if __name__ == "__main__":

    print("-"*35)
    String = input("Enter a string : ")
    print("-"*35)
    print(f"The entered string is : {String}")
    print("-"*35)
    
    t1 = threading.Thread(target= Small,args= (String,),name = "SmallThread")
    t2 = threading.Thread(target= Capital,args= (String,),name = "CapitalThread")
    t3 = threading.Thread(target= Digits,args= (String,),name = "DIgitsThread")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("three threads are executed successfully")
    print("-"*35)
    print("Exit from main")
    print("-"*35)


import threading

def DisplayEven():

    print("Thread Name : ",threading.current_thread().name)

    print("ID : ",threading.get_ident())
    
    
    count = 0
    num = 1
    ResEven = []

    while count < 10:
        if num % 2 == 0 :
            ResEven.append(num)
            count = count + 1
        num = num + 1

    print("first 10 Even numbers are : ",ResEven)

def DisplayOdd():

    print("Thread Name : ",threading.current_thread().name)

    print("ID : ",threading.get_ident())
    
    count = 0
    num = 1
    Resodd = []

    while count < 10:
        if num % 2 != 0 :
            Resodd.append(num)
            count = count + 1
        num = num + 1

    print("first 10 Odd numbers are : ",Resodd)

if __name__ == "__main__":

    t1 = threading.Thread(target = DisplayEven,name = "Eventhread")
    t2 = threading.Thread(target = DisplayOdd,name = "Oddthread")

    t1.start()
    t2.start()

    t1.join()
    t2.join()



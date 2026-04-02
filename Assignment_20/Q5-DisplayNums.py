import threading

def Display():
    print(f"ThreadName = {threading.current_thread().name} and ThreadID = {threading.get_ident()}")
    Data = list()
    for i in range(1,50+1):
        Data.append(i)
    print(Data)

def DisplayRev():
    print(f"ThreadName = {threading.current_thread().name} and ThreadID = {threading.get_ident()}")
    Data = list()
    for i in range(50,0,-1):
        Data.append(i)
    print(Data)


if __name__ == "__main__":

    t1 = threading.Thread(target= Display,name = "DisplaY(1-50)")
    t2 = threading.Thread(target= DisplayRev,name = "DisplaY(50-1)")

    #Ensure that:
         #Thread2 starts execution only after Thread1 has completed.

    t1.start()
    t1.join()
    

    t2.start()
    t2.join()

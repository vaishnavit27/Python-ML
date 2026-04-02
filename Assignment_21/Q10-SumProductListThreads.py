import threading

#Return the results to the main thread and display them.



def Sum(Data,results_dict):

    Sum = 0
    for i in Data:
        Sum = Sum + i

    results_dict['Sum'] = Sum
    

def Product(Data,results_dict):

    Product = 1
    for i in Data:
        Product = Product * i 

    results_dict['Product'] = Product

if __name__ == "__main__":

    Size = 0

    print("Enter the number of elements : ")
    Size = int(input())

    Data = []

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    results = {}

    t1 = threading.Thread(target= Sum , args= (Data,results) , name = "SumThread")
    t2 = threading.Thread(target= Product , args= (Data,results) , name = "ProductThread")

    t1.start()
    t2.start()

    t1.join()
    
    t2.join()

    print("Sum:", results['Sum'])
    print("Product:", results.get('Product'))

    

    print("Exit from main")
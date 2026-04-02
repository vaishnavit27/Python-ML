import pandas as pd


data = pd.read_csv("student_performance_ml.csv")

print("First 5 records : ")
print(data.head(5))

print("Last 5 records : ")
print(data.tail(5))

print("Total number of rows and columns : ")
print(data.shape)


print("List of column names : ")
Ret = list(data.columns)
print(Ret)

print("Data types of each columns : ")

print(data.dtypes)    # data types of every column




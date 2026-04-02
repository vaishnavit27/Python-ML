import pandas as pd

df=pd.read_csv("student_performance_ml.csv")

print("Total number of students are : " ,len(df.index))
# print(len(df))
# print(df.shape[0])


Ret = (df["FinalResult"]==1).sum()
print("Total Number of students passed are : ",Ret)

Ret = (df["FinalResult"]==0).sum()
print("Total Number of students passed are : ",Ret)




    

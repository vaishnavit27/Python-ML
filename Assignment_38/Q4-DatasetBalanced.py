import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

print(df["FinalResult"].value_counts())

Pass = ((df["FinalResult"]==1).sum())
print("Passed students",Pass)

Fail = ((df["FinalResult"]==0).sum())
print("Failed students",Pass)

Ret = (len(df["FinalResult"]))
print("Total Final result students",Ret)

print("Passed students : ",(Pass / Ret )*100)

print("Failed students : ",(Fail / Ret )*100)

"""
Hence the dataset is not balanced : Because the target column contains ratio of 60:40 for pass and fail students classes respectively
And a Dataset is considered Balanced when the classes are represented in equal or roughly equal proportions
"""

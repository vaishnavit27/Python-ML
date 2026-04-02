import pandas as pd

df=pd.read_csv("student_performance_ml.csv")

print("Average of StudyHours is : ",df["StudyHours"].mean().round(2))

print("Average of Attendance is : ",df["Attendance"].mean().round(2))

print("Maximum Previous Score is : ",df["PreviousScore"].max())

print("Minimum SleepHours is : ",df["SleepHours"].min())
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("student_performance_ml.csv")

sns.scatterplot(x = df["FinalResult"],y = df["StudyHours"])
plt.show()
import numpy as np
import pandas as pd
from scipy import stats


data = np.array(pd.read_csv("Salary_Data.csv"))



n = len(data[0])
print("Mean :-",end="\t")
for i in range(n) : print(np.mean(data[:,i]),end="\t")
print("\nMedian :-",end="\t")
for i in range(n) : print(np.median(data[:,i]),end="\t")
print("\nMode :-",end="\t")
for i in range(n) : print(stats.mode(data[:,i]).mode,end="\t")
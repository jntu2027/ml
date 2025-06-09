import numpy as np
import pandas as pd
from scipy import stats

data = np.array(pd.read_csv("Salary_Data.csv"))

n = len(data[0])
print("Median :- ",end="\t")
for i in range(n) : print(np.median(data[:,i]),end="\t")
print("\nStandard Deviation :- ",end="\t")
for i in range(n) : print(np.std(data[:,i]),end="\t")
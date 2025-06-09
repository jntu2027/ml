import pandas as pd
import numpy as np

data = pd.read_csv("enjoysport.csv")
data = np.array(data)

number_of_features = len(data[0]) - 1    # -1 to remove the final value

SpecificHypothesis = ["O" for i in range(number_of_features)]

for row in data:
    if (row[-1] == "yes") :
        
        for i in range(number_of_features):
            if (SpecificHypothesis[i] == "O"):
                SpecificHypothesis[i] = row[i]
            elif (SpecificHypothesis[i] != row[i]):
                SpecificHypothesis[i] = "?"
        
print("The input data: ")
print("   sky   airtemp humidity  wind   water  forcast  enjoysport")
print(data)
print("The Specific Hypothesis :- ",end="")
print(SpecificHypothesis)
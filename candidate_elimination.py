import pandas as pd
import numpy as np

data = pd.read_csv("enjoysport.csv")
data = np.array(data)

number_of_features = len(data[0]) - 1    # -1 to remove the final value

SpecificHypothesis = ["O" for i in range(number_of_features)]
GeneralHypothesis = set()
GeneralHypothesis.add(tuple("?" for i in range(number_of_features)))

for row in data:
    if (row[-1] == "yes"):
        
        for i in range(number_of_features):
            if (SpecificHypothesis[i] == "O"):
                SpecificHypothesis[i] = row[i]
            elif (SpecificHypothesis[i] != row[i]):
                SpecificHypothesis[i] = "?"
                
        new_GH = GeneralHypothesis.copy()
        for g in new_GH:
            for i in range(number_of_features):
                if  (g[i] != "?" and g[i] != row[i]):
                    GeneralHypothesis.remove(g)
                    break
    
    else:
        new_GH = GeneralHypothesis.copy()
        for g in new_GH:
            flag = True
            for i in range(number_of_features):
                if  (g[i] != "?" and g[i] != row[i]):
                    flag = False
                    break
            if (flag):
                GeneralHypothesis.remove(g)
        
        for i in range(number_of_features):
            if (SpecificHypothesis[i] != "?" and SpecificHypothesis[i] != row[i]):
                new = ["?" for j in range(number_of_features)]
                new[i] = SpecificHypothesis[i]
                GeneralHypothesis.add(tuple(new))

print("The input data: ")
print("   sky   airtemp humidity  wind   water  forcast  enjoysport")
print(data)
print("The Specific Hypothesis :- ",end="")
print(SpecificHypothesis)
print("The General Hypothesis :- ",end="")
print(GeneralHypothesis)
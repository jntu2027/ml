from sklearn import tree
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("PlayTennis.csv")

x = data.iloc[:,:-1]
y = data.iloc[:,-1]

x = pd.get_dummies(x)

model = tree.DecisionTreeClassifier(criterion="entropy").fit(x,y)
tree.plot_tree(model,feature_names= x.columns)
plt.show()
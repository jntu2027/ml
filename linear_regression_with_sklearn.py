import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression


data = pd.read_csv("Salary_Data.csv")
data = np.array(data)
x = data[:,:-1]
y = data[:,-1]


model = LinearRegression()
model.fit(x,y)
y_pred = model.predict(x)
    
plt.scatter(x,y , color = 'blue',label = "Actual")
plt.plot(x, y_pred , color = 'black' , label = "predicted")
plt.xlabel("Exprience")
plt.ylabel("Salary")
plt.title("simple linear regression")
plt.legend()
plt.show()
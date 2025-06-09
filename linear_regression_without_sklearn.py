import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("Salary_Data.csv")
data = np.array(data)
x = data[:,:-1]
y = data[:,-1]
n = len(x)
x_mean = np.mean(x)
y_mean = np.mean(y)

# y = wx + b
#    ((x-x_mean)*(y-y_mean))/ (x-x_mean)^2
numerator =  np.sum( [(x[i] - x_mean)*(y[i] - y_mean)  for i in range(n)])
denominator = np.sum( [  (x[i] - x_mean)**2  for i in range(n)  ])
w = numerator/denominator

b = y_mean - w*x_mean

y_pred = [ (w*x[i] + b) for i in range(n) ]

for i in range(n):
    print(y_pred[i],y[i],sep="\t")
    

    
    
plt.scatter(x,y , color = 'blue',label = "Actual")
plt.plot(x, y_pred , color = 'green' , label = "predicted")
plt.xlabel("Exprience")
plt.ylabel("Salary")
plt.title("simple linear regression")
plt.legend()
plt.show()
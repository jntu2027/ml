import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Perceptron

# OR dataset
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
y = np.array([0, 1, 1, 1])  

clf = Perceptron(tol=1e-3, random_state=0)
clf.fit(X, y)

w = clf.coef_[0]
b = clf.intercept_

plt.figure(figsize=(6, 6))

for i in range(len(X)):
    color = 'green' if y[i] == 1 else 'red'
    plt.scatter(X[i][0], X[i][1], color=color, s=100, edgecolors='k')

x_vals = np.linspace(-0.5, 1.5, 100)
if w[1] != 0:
    y_vals = -(w[0] * x_vals + b) / w[1]
    plt.plot(x_vals, y_vals, 'b--', label="Decision Boundary")
else:
    plt.axvline(-b / w[0], color='b', linestyle='--', label="Decision Boundary")

plt.title("Perceptron Classifier for OR Gate")
plt.xlabel("Input 1")
plt.ylabel("Input 2")
plt.grid(True)
plt.legend()
plt.xlim(-0.5, 1.5)
plt.ylim(-0.5, 1.5)
plt.show()

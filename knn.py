import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

X, y = load_iris(return_X_y=True)
X = X[:, :2]

knn = KNeighborsClassifier(n_neighbors=5).fit(X, y)
x_min, x_max = X[:, 0].min()-1, X[:, 0].max()+1
y_min, y_max = X[:, 1].min()-1, X[:, 1].max()+1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.4, cmap='coolwarm')
for i, color in zip(np.unique(y), ['red', 'green', 'blue']):
    plt.scatter(X[y == i, 0], X[y == i, 1], label=f"Class {i}", color=color, edgecolor='k')
plt.xlabel("Feature 1"), plt.ylabel("Feature 2")
plt.title("KNN Decision Boundaries"), plt.legend()
plt.show()
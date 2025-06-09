import numpy as np
import matplotlib.pyplot as plt

X = np.array([
    [2, 7],
    [3, 6],
    [4, 5],
    [5, 8],
    [6, 7],
    [7, 6],
    [8, 5],
    [9, 7],
    [10, 8],
    [11, 6]
])
y = np.array([55, 58, 60, 70, 75, 78, 82, 88, 92, 95])

w = np.linalg.inv(X.T @ X) @ X.T @ y
print("Weights:", w)

y_pred = X @ w

feature_names = ['StudyHours', 'SleepHours']
n_features = len(X[0])
fixed_values = np.mean(X, axis=0)
if n_features > 1:
    fig, axs = plt.subplots(1, n_features, figsize=(6 * n_features, 5))


    fig.suptitle("Feature Effect (Partial Dependence View)", fontsize=14)

    for i in range(n_features):
        x_range = np.linspace(X[:, i].min(), X[:, i].max(), 100)
        X_input = np.tile(fixed_values, (100, 1))
        X_input[:, i] = x_range 

        y_line = X_input @ w 

        axs[i].scatter(X[:, i], y, color='blue', label='Actual')
        axs[i].plot(x_range, y_line, color='red', label='Predicted (w.r.t. this feature)')
        axs[i].set_xlabel(feature_names[i])
        axs[i].set_ylabel("Target")
        axs[i].legend()
        axs[i].grid(True)

    plt.tight_layout(rect=[0, 0, 1, 0.93])
    plt.show()
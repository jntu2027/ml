import matplotlib.pyplot as plt
import numpy as np
import random

data = [
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
]

n = float(input("Enter the learning rate (0.01 - 0.1): \t"))
epochs = int(input('Enter the number of epochs (100 - 300):\t'))

w1 = random.uniform(-0.5,0.5)
w2 = random.uniform(-0.5,0.5)
bias = random.uniform(-0.5,0.5)

def step_function(z):
    return 1 if z >= 0 else 0

for epoch in range(epochs):
    for x1, x2, target in data:
        z = w1 * x1 + w2 * x2 + bias
        y_pred = step_function(z)
        error = target - y_pred
        w1 += n * error * x1
        w2 += n * error * x2
        bias += n * error

print(f"Trained weights: w1={w1:.3f}, w2={w2:.3f}, bias={bias:.3f}")

for x1, x2, label in data:
    if label == 1 :
        color = 'blue' 
    else :
        color = 'red'
    plt.scatter(x1, x2, color=color)

x_vals = np.linspace(-0.1, 1.1, 100)
if w2 != 0:
    y_vals = -(w1 / w2) * x_vals - (bias / w2)
    plt.plot(x_vals, y_vals, color='green', label='Decision Boundary')
else:
    plt.axvline(-bias / w1, color='green', label='Decision Boundary')

plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Perceptron')
plt.legend()
plt.grid(True)
plt.show()

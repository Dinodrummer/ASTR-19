import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
def f(x, a, b):
    return a * np.exp(-b * x)

a = 10
b = 7
y = f(x, a, b)

sigma = np.linspace(2, 0.2, len(x))
noise = np.random.normal(0, sigma)
y_scattered = y + noise

plt.errorbar(x, y_scattered, color='green', yerr=sigma, fmt='o', markersize=3, capsize=2, label='Scattered Data')
plt.plot(x, y, color='red', linestyle='--')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
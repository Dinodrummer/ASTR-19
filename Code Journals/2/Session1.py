from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
def f(x,a,b):
    return a * np.exp(-b * x)
a = 10
b = 7

y = f(x, a, b)

plt.plot(x,y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
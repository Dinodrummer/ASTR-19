import numpy as np
from matplotlib import pyplot as plt
rng = np.random.default_rng()

x = rng.standard_normal(1000)

plt.hist(x, bins=100, color='green')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Histogram of 1000 Standard Normal Random Numbers')

plt.show()

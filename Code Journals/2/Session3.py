import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

x = np.linspace(0.1, 2 * np.pi, 100)
y = np.linspace(0.1, 2 * np.pi, 100)

def f(x, a, b):
    return a * np.exp(-b * x)

def p(x, a, b):
    return a / (x**b)

at = 10
bt = 7
yt = f(x, at, bt)
sigma = np.linspace(0.1, 2 * np.pi, 100)
ys = yt + np.random.normal(0, sigma)

opt_f, cov_f = curve_fit(f,x,ys, p0 = [10,5], sigma = sigma)
opt_p, cov_p = curve_fit(p,x,ys, p0 = [1,1], sigma = sigma)

print(f"Exponential: a = {opt_f[0]:.4f}, b = {opt_f[1]:.4f}")
print(f"Power: a = {opt_p[0]:.4f}, b = {opt_p[1]:.4f}")

plt.errorbar(x, ys, yerr=sigma, fmt='o', color='black', markersize=2, capsize=2, alpha = 0.2, label='Scattered Data')

plt.plot(x, f(x, *opt_f), color='red', label=f'Exponential Fit (a={opt_f[0]:.2f}, b={opt_f[1]:.2f})')

plt.plot(x, p(x, *opt_p), color='blue', label=f'Power Fit (a={opt_p[0]:.2f}, b={opt_p[1]:.2f})')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Best Fit Models Comparison')
plt.legend()
plt.ylim(-10, 20)  # Constrain y-axis to see data clearly
plt.show()
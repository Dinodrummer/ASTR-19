import numpy as np
from astropy.table import Table

def main():
    x = np.linspace(0, 2*np.pi, 1000)
    sin_x = np.sin(x)
    t = Table([x, sin_x], names=['x', 'sin(x)'])
    print(t)

if __name__ == '__main__':
    main()
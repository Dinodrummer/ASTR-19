import sys
import numpy as np

# return cartesian distance of (x1,y1) and (x2,y2)
def cartesian_dist(x1,y1,x2,y2):
    #size of triangle corresponding to x-axis and y-axis
    dx = x1 - x2
    dy = y1 - y2
    ds = np.sqrt(dx**2 + dy**2)

    return ds

def main():
    x1 = 5 * np.random.random(10)
    x2 = 5 * np.random.random(10)
    y1 = 5 * np.random.random(10)
    y2 = 5 * np.random.random(10)

    ds = cartesian_dist(x1,y1,x2,y2)

    for i in range(len(x1)):
        print("The", i, "element of list 2 has coordinates x=", x1[i], ", y =", y1[i])
        print("The", i, "element of list 2 has coordinates x=", x2[i], ", y =", y2[i])

if __name__ == '__main__':
    main()
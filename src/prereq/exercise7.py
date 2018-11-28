import numpy as np
import matplotlib.pyplot as plt

# Plot concentric circles dataset

def getCircleData(r):
    r_with_epsilon = r * (1 + np.random.rand(250) / 7)
    theta = 2 * np.pi * np.random.rand(250)

    x = r_with_epsilon * np.cos(theta)
    y = r_with_epsilon * np.sin(theta)

    return (x, y)

def main():
    xlg, ylg = getCircleData(20)
    xsm, ysm = getCircleData(10)

    plt.scatter(xlg, ylg, c='b')
    plt.scatter(xsm, ysm, c='r')

    plt.show()

if __name__ == '__main__':
    main()

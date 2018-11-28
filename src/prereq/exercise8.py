import numpy as np
import matplotlib.pyplot as plt

# Plot a spiral dataset

def generateArm(rotation, step):
    theta = np.random.rand(500) * step
    r = np.exp(theta) - 1

    x = r * np.cos(theta) + (np.random.rand(500) - 0.5) / 7
    y = r * np.sin(theta) + (np.random.rand(500) - 0.5) / 7

    x, y = x * np.cos(rotation) - y * np.sin(rotation), x * np.sin(rotation) + y * np.cos(rotation)

    return (x, y)

def main():
    arms = 6
    step = 2 * np.pi / arms

    for i in range(arms):
        rotation = i * step

        x, y = generateArm(rotation, step)

        plt.scatter(x, y)

    plt.show()

if __name__ == '__main__':
    main()

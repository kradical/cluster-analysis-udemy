import numpy as np
import matplotlib.pyplot as plt

# Plot the XOR dataset

def main():
    x = 2 * np.random.rand(7500) - 1;
    y = 2 * np.random.rand(7500) - 1;

    xor = np.logical_xor(x > 0, y > 0)

    c = ['r' if x else 'b' for x in xor]

    plt.scatter(x, y, c=c)

    plt.show()

if __name__ == '__main__':
    main()

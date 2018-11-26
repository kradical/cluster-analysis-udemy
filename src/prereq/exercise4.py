from time import perf_counter

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Rotating an image 90 degrees
# Time the difference between for loops and numpy methods

def plotImage(fig, rawImg, i):
    img = rawImg.reshape(28, 28)

    sub = fig.add_subplot(3, 4, i + 1)
    sub.set_xticks([])
    sub.set_yticks([])

    plt.imshow(img)

def forRotation(img):
    newImage = np.zeros(img.shape)

    maxX = img.shape[0]
    maxY = img.shape[1]

    for x in range(maxX):
        for y in range(maxY):
            newX = maxY - y - 1
            newY = x

            newImage[newX, newY] = img[x, y]

    return newImage

def perfTest(rotation, img):
    rotated = img

    t = perf_counter()

    for i in range(1000):
        rotated = rotation(img)

    dt = perf_counter() - t
    print('avg', rotation.__name__, 'runtime:', dt / 100)

    return rotated

def main():
    df = pd.read_csv('../../data/digits.csv')

    grouped = df.groupby('label').mean()
    img = np.array(grouped)[8].reshape(28, 28)

    rotatedFor = perfTest(forRotation, img)
    rotatedNp = perfTest(np.rot90, img)

    fig=plt.figure()

    plotImage(fig, rotatedFor, 1)
    plotImage(fig, rotatedNp, 2)

    plt.show()

if __name__ == '__main__':
    main()

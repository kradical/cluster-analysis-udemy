import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Show the average of every hand written digit from the data set

def plotImage(fig, rawImg, i):
    img = rawImg.reshape(28, 28)

    sub = fig.add_subplot(3, 4, i + 1)
    sub.set_xticks([])
    sub.set_yticks([])

    plt.imshow(img)

def main():
    df = pd.read_csv('../../data/digits.csv')

    grouped = df.groupby('label').mean()

    averages = np.array(grouped)

    fig=plt.figure()

    for i, a in enumerate(averages):
        plotImage(fig, a, i)

    plt.show()

if __name__ == '__main__':
    main()

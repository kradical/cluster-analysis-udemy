import numpy as np
import pandas as pd

# Save 3D dataset to pandas

def main():
    x = 2 * np.random.rand(7500) - 1;
    y = 2 * np.random.rand(7500) - 1;

    xor = np.logical_xor(x > 0, y > 0)

    c = ['r' if x else 'b' for x in xor]

    df = pd.DataFrame({
        'x': x,
        'y': y,
        'c': c,
    })

    df.to_csv('../../data/exercise9.csv')

if __name__ == '__main__':
    main()

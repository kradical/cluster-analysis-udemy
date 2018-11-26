import numpy as np
import matplotlib.pyplot as plt

# Look at the central limit theorem numerically!

data = np.random.rand(10000, 10000)

sums = data.sum(axis=1)

plt.hist(sums, bins=100)
plt.show()

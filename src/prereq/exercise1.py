import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [0.3, 0.6, 0.1],
    [0.5, 0.2, 0.3],
    [0.4, 0.1, 0.5],
])

v = np.array([1/3, 1/3, 1/3])

data = []

for i in range(25):
    vn = v.dot(A)

    norm = np.linalg.norm(vn - v)
    data.append(norm)

    v = vn

print(v)
plt.plot(data)
plt.show()

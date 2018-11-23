import numpy as np
from datetime import datetime

a = np.random.randn(100)
b = np.random.randn(100)

iterations = 10000

# Slow way
t0 = datetime.now()

for i in range(iterations):
    result = 0
    for e, f in zip(a, b):
        result += e * f

dt0 = datetime.now() - t0

print("without numpy:", dt0)

# numpy way
t1 = datetime.now()

for i in range(iterations):
    result = a.dot(b)

dt1 = datetime.now() - t1

print("with numpy:", dt1)

print("numpy is ", dt0 / dt1, " times faster!")

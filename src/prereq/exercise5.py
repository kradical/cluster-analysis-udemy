from time import perf_counter

import numpy as np

# Testing if a matrix is symmetric
# Time the difference between for loops and numpy methods

def forSymmetric(M):
    for i in range(1, M.shape[0]):
        for j in range(0, i):
            if (M[i, j] != M[j, i]):
                return False

    return True

def npSymmetric(M):
    return np.allclose(M, M.T)

def generateSymmetric():
    b = np.random.rand(100, 100)
    return (b + b.T) / 2

def generateAsymmetric():
    return np.random.rand(100, 100)

def perfTest(method, arg):
    computed = None

    t = perf_counter()

    for i in range(100):
        computed = method(arg)

    dt = perf_counter() - t
    print('avg', method.__name__, 'runtime:', dt / 100)

    return computed

def main():
    print('symmetric runtimes:')
    symmetric = generateSymmetric()
    symmetricFor = perfTest(forSymmetric, symmetric)
    symmetricNp = perfTest(npSymmetric, symmetric)
    print()

    print('asymmetric runtimes:')
    asymmetric = generateAsymmetric()
    asymmetricFor = perfTest(forSymmetric, asymmetric)
    asymmetricNp = perfTest(npSymmetric, asymmetric)
    print()

    print('Results:')
    print('symmetricFor', symmetricFor)
    print('symmetricNp', symmetricNp)
    print('asymmetricFor', asymmetricFor)
    print('asymmetricNp', asymmetricNp)

if __name__ == '__main__':
    main()

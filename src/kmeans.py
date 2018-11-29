import numpy as np
import matplotlib.pyplot as plt

def d(u, v):
    diff = u - v
    return diff.dot(diff)

def cost(X, R, M):
    cost = 0
    for k in range(len(M)):
        for n in range(len(X)):
            cost += R[n,k]*d(M[k], X[n])

    return cost

def plot_k_means(X, K, max_iter=20, beta=1.0):
    N, D = X.shape

    M = np.array(
        X[np.random.choice(N, K, replace=False), :]
    )

    R = np.zeros((N, K))

    costs = np.zeros(max_iter)
    for i in range(max_iter):
        # recalculate responsibility
        for k in range(K):
            for n in range(N):
                denomIter = (np.exp(-beta * d(M[j], X[n])) for j in range(K))
                numExp = -beta * d(M[k], X[n])

                R[n,k] = np.exp(numExp) / np.sum(np.fromiter(denomIter, float))

        # recalculate the means
        for k in range(K):
            M[k] = R[:,k].dot(X) / R[:,k].sum()

        # calculate cost and break if it hasn't changed much
        costs[i] = cost(X, R, M)
        if i > 0 and np.abs(costs[i] - costs[i-1]) < 0.1:
            break

    random_colors = np.random.random((K, 3))
    colors = R.dot(random_colors)

    plt.scatter(X[:,0], X[:,1], c=colors)
    plt.show()

def main():
    D = 2
    s = 4 # distance between means

    mean1 = np.array([0, 0])
    mean2 = np.array([s, s])
    mean3 = np.array([0, s])

    samples = 900
    data = np.zeros((samples, D))

    # generate the dataset
    data[:300, :] = np.random.randn(300, D) + mean1
    data[300:600, :] = np.random.randn(300, D) + mean2
    data[600:, :] = np.random.randn(300, D) + mean3

    clusters = 3
    plot_k_means(data, clusters)

    # clusters = 5
    # plot_k_means(data, clusters, max_iter=30)

    # clusters = 5
    # plot_k_means(data, clusters, max_iter=30, beta=0.3)

if __name__ == '__main__':
    main()

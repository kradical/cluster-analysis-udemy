import numpy as np
import matplotlib.pyplot as plt

def squareDistance(u, v):
    diff = u - v
    return diff.dot(diff)

# We want to minimize intra-cluster variance (squard error)
def objective(X, R, M):
    cost = 0
    for k in range(len(M)):
        for n in range(len(X)):
            cost += R[n,k] * squareDistance(M[k], X[n])

    return cost

def expDistance(p1, p2, beta):
    return np.exp(-beta * squareDistance(p1, p2))

def plot_k_means(X, K, max_iter=20, beta=1.0):
    N, D = X.shape

    M = np.array(
        X[np.random.choice(N, K, replace=False), :]
    )

    R = np.zeros((N, K))

    costs = np.zeros(max_iter)
    for i in range(max_iter):
        # calculate responsibility for each point for each cluster
        for k in range(K):
            for n in range(N):
                sumMeanDistances = np.array([
                    expDistance(M[j], X[n], beta) for j in range(K)
                ]).sum()

                meanDistance = expDistance(M[k], X[n], beta)

                softMax = meanDistance / sumMeanDistances

                R[n,k] = softMax

        # calculate the means for each cluster
        for k in range(K):
            M[k] = R[:,k].dot(X) / R[:,k].sum()

        # calculate cost and break if it hasn't changed much
        costs[i] = objective(X, R, M)
        if i > 0 and np.abs(costs[i] - costs[i - 1]) < 0.1:
            break

    # pick K random RGB values to represent clusters
    random_colors = np.random.random((K, 3))
    # weight the color of a point based on its responsibility to each cluster.
    colors = R.dot(random_colors)

    plt.scatter(X[:,0], X[:,1], c=colors)
    plt.show()

def generate_samples():
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

    return data

def main():
    data = generate_samples()

    clusters = 3
    plot_k_means(data, clusters)

    # clusters = 5
    # plot_k_means(data, clusters, max_iter=30)

    # clusters = 5
    # plot_k_means(data, clusters, max_iter=30, beta=0.3)

if __name__ == '__main__':
    main()

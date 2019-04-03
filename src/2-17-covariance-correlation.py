import numpy as np
import matplotlib.pyplot as plt


def de_mean(x):
    x_mean = np.mean(x)
    return [xi - x_mean for xi in x]


def covariance(x, y):
    n = len(x)
    return np.dot(de_mean(x), de_mean(y)) / (n - 1)


def correlation(x, y):
    std_dev_x = x.std()
    std_dev_y = y.std()
    return covariance(x, y) / std_dev_x / std_dev_y


pageSpeeds = np.random.normal(3, 1, 1000)
# purchaseAmount = np.random.normal(50, 10, 1000)
# purchaseAmount = np.random.normal(50, 10, 1000) / pageSpeeds
purchaseAmount = 100 - pageSpeeds * 3

plt.scatter(pageSpeeds, purchaseAmount)
plt.show()

cov = covariance(pageSpeeds, purchaseAmount)
print('covariance by func: {0}'.format(cov))

cov = np.cov(pageSpeeds, purchaseAmount)
print('covariance by numpy: {0}'.format(cov))

cor = correlation(pageSpeeds, purchaseAmount)
print('correlation by func: {0}'.format(cor))

cor = np.corrcoef(pageSpeeds, purchaseAmount)
print('correlation by numpy: {0}'.format(cor))


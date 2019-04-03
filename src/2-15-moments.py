import numpy as np
import scipy.stats as sp
import matplotlib.pyplot as plt

values = np.random.normal(0, 0.5, 10000)
#plt.hist(values, 50)
#plt.show()

mean = np.mean(values)
print('mean: {0}'.format(mean))

variance = np.var(values)
print('variance: {0}'.format(variance))

skew = sp.skew(values)
print('skew: {0}'.format(skew))

kurtosis = sp.kurtosis(values)
print('kurtosis: {0}'.format(kurtosis))
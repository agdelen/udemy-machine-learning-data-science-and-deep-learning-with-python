import numpy as np
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

np.random.seed(2)
pageSpeeds = np.random.normal(3, 1, 1000)
purchaseAmount = np.random.normal(50, 10, 1000) / pageSpeeds

# plt.scatter(pageSpeeds, purchaseAmount)
# plt.show()

x = np.array(pageSpeeds)
y = np.array(purchaseAmount)
p4 = np.poly1d(np.polyfit(x, y, 4))

xp = np.linspace(0, 7, 100)
plt.scatter(x, y)
plt.plot(xp, p4(xp), c='r')
plt.show()

r2 = r2_score(y, p4(x))
print('r-squared: {0}'.format(r2))

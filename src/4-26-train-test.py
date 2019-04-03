import numpy as np
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

np.random.seed(2)
pageSpeeds = np.random.normal(3, 1, 100)
purchaseAmount = np.random.normal(50, 30, 100) / pageSpeeds

# plt.scatter(pageSpeeds, purchaseAmount)

trainX = pageSpeeds[:80]
testX = pageSpeeds[80:]

trainY = purchaseAmount[:80]
testY = purchaseAmount[80:]

# plt.scatter(trainX, trainY)
# plt.scatter(testX, testY)
# plt.show()

x = np.array(trainX)
y = np.array(trainY)

p8 = np.poly1d(np.polyfit(x, y, 6))

xp = np.linspace(0, 7, 100)
axes = plt.axes()
axes.set_xlim([0, 7])
axes.set_ylim([0, 200])
plt.scatter(x, y)
plt.plot(xp, p8(xp), c='y')
# plt.show()


testx = np.array(testX)
testy = np.array(testY)

axes = plt.axes()
axes.set_xlim([0, 7])
axes.set_ylim([0, 200])
plt.scatter(testx, testy)
plt.plot(xp, p8(xp), c='r')
plt.show()

r2train = r2_score(y, p8(x))
print('r-squared train: {0}'.format(r2train))

r2test = r2_score(testy, p8(testx))
print('r-squared test: {0}'.format(r2test))

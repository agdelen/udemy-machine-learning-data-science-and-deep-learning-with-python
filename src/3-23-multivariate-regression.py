import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()

df = pd.read_excel('http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls')
# print(df.head())
# df.info()

X = df[['Mileage', 'Cylinder', 'Doors']]
y = df['Price']

X[['Mileage', 'Cylinder', 'Doors']] = scale.fit_transform(X[['Mileage', 'Cylinder', 'Doors']].values)

print(X)

est = sm.OLS(y, X).fit()
print(est.summary())

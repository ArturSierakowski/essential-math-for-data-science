import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",")

X = df.values[:, :-1]
Y = df.values[:, -1]
print(X)
print(Y)

dopasowanie = LinearRegression().fit(X, Y)

m = dopasowanie.coef_.flatten()
b = dopasowanie.intercept_.flatten()
print("m = {0}".format(m))
print("b = {0}".format(b))

plt.plot(X, Y, 'o')
plt.plot(X, m*X+b)
plt.show()

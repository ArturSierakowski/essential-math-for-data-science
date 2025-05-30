import pandas as pd

punkty = list(pd.read_csv('https://bit.ly/3goOAnt', delimiter=",").itertuples())

n = len(punkty)

m = (n*sum(p.x*p.y for p in punkty) - sum(p.x for p in punkty) * sum(p.y for p in punkty)) / \
    (n*sum(p.x**2 for p in punkty) - sum(p.x for p in punkty)**2)

b = (sum(p.y for p in punkty) / n) - m * sum(p.x for p in punkty) / n

print(m, b)

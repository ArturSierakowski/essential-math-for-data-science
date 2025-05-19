import pandas as pd

points = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",").itertuples()

m = 1.93939
b = 4.73333

suma_kwadratow = 0

for p in points:
    y_rzeczywista = p.y
    y_przewidywana = m*p.x + b
    reszta_kwadrat = (y_rzeczywista - y_przewidywana)**2
    suma_kwadratow += reszta_kwadrat

print(format(suma_kwadratow, '.2f'))

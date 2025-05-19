from sympy import *

x, i, n = symbols('x i n')

f = x**2 + 1
dolny, gorny = 0, 1

delta_x = (gorny - dolny) / n
x_i = (dolny + delta_x * i)
fx_i = f.subs(x, x_i)


liczba_prostokatow = Sum(delta_x * fx_i, (i, 1, n)).doit()

pole = limit(liczba_prostokatow, n, oo)

print(pole)

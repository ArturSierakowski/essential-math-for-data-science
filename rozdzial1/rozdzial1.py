import numpy as np
from sympy import *

# ODSETKI Z POZYCZKI

# odsetki_co_miesiac = 1000 * (1 + 0.05 / 12)**36
# odsetki_co_rok = 1000 * 1.05**3
#
# print(odsetki_co_miesiac)
# print(odsetki_co_rok)
#
# odsetki_ciagle = 1000 * np.e**0.15
#
# print(odsetki_ciagle)

# LUB

# P, r, n, t = symbols('P r n t')
#
# A = P * (1 + r / n)**(t * n)
#
# P_wartosc = 1000
# r_wartosc = 3
# t_wartosc = 0.05
#
# granica = limit(A, n, oo)
# pozyczka = granica.subs({P: P_wartosc, r: r_wartosc, t: t_wartosc})
#
# print(pozyczka)

# NACHYLENIE (POCHODNA)

# x = symbols('x')
#
# f = 3 * x**2 + 1
# dx_f = diff(f)
# print(dx_f)
# print(dx_f.subs(x, 3))

# POLE POD KRZYWA (CALKA)

x = symbols('x')

f = 3 * x**2 + 1
pole = integrate(f, (x, 0, 2))
print(pole)

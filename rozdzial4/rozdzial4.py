from numpy import array
from numpy.linalg import inv
from sympy import *

A = array([
    [3, 1, 0],
    [2, 4, 1],
    [3, 1, 8]
])

B = array([54, 12, 6])

wynik = inv(A) @ B
print(wynik)


baza = Matrix([
    [2, 1],
    [6, 3]
])

wyznacznik = det(baza)
print(wyznacznik)

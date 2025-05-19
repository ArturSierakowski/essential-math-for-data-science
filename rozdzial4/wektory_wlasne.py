from numpy import array, diag
from numpy.linalg import eig, inv

A = array([
    [1, 2],
    [4, 5]
])

wart_wlasne, wekt_wlasne = eig(A)

# print("Wartosci wlasne")
# print(wart_wlasne)
# print("Wektory wlasne")
# print(wekt_wlasne)

Q = wekt_wlasne
R = inv(Q)

L = diag(wart_wlasne)
B = Q @ L @ R

print(Q)
print(L)
print(R)

print(B)

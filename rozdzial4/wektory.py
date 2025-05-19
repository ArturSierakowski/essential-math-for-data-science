import numpy as np
from numpy import array

# MNOZENIE WEKTOROW

# baza = np.array(
#     [[3, 0],
#      [0, 2]]
# )
#
# v = np.array([1, 1])
#
# nowy_v = baza.dot(v)
#
# print(baza)
# print(v)
# print(nowy_v)

# i_daszek = np.array([2, 0])
# j_daszek = np.array([0, 3])
#
# baza = np.array([i_daszek, j_daszek]).T
#
# v = np.array([1, 1])
#
# nowy_v = baza.dot(v)
#
# print(nowy_v)

# BARDZIEJ SKOMPLIKOWANE

# i_daszek = np.array([2, 3])
# j_daszek = np.array([2, -1])
#
# baza = np.array([i_daszek, j_daszek]).T
#
# v = np.array([1, 1])
#
# nowy_v = baza.dot(v)
#
# print(nowy_v)

# OBROT I SCIECIE

obrocenie = array([[0, 1], [-1, 0]]).T
sciecie = array([[1, 0], [1, 1]]).T
polaczone = sciecie @ obrocenie
print("polaczona macierz:\n {}".format(polaczone))

v = [1, 2]

polaczony_v = polaczone @ v

print(polaczony_v)

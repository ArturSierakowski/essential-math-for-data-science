from scipy.stats import binom, beta

# PASAZEROWIE, LOT

# k = 50
# n = 137
# p = 0.4
#
# prawdopodobienstwo = 0
#
# # nie pojawi sie przynajmniej 50 = pojawi sie co najwyzej 49
# for i in range(k):
#     prawdopodobienstwo += binom.pmf(i, n, p)
#
# print(prawdopodobienstwo)

# RZUT MONETA

a = 15
b = 4

p = beta.cdf(0.5, 15, 4)

print(p)

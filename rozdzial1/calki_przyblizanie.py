def przybliz_calke(a, b, n, f):
    # szerokosc jednego z prostokatow / odleglosc pomiedzy prostokatami, inaczej ich srodkami
    delta_x = (b - a) / n
    suma = 0

    for i in range(0, n):
        #
        pkt_srodkowy = a + delta_x * (i + 1/2)
        suma += f(pkt_srodkowy)

    return suma * delta_x


def moja_funkcja(x):
    return x**2 + 1


pole = przybliz_calke(0, 1, 1000, moja_funkcja)
print(pole)

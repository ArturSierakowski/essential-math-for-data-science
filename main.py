import numpy as np
import matplotlib.pyplot as plt

# Dane
x = np.linspace(1, 100, 400)  # Czas/wysiłek od 1 do 100
y = 50 * np.log10(x)  # Logarytm dziesiętny

# Tworzenie wykresu
plt.figure(figsize=(8, 4))
plt.plot(x, y, label='y = 15 * log2(x)')
plt.title('Zależność między wysiłkiem a rezultatami')
plt.xlabel('Wysiłek/Czas')
plt.ylabel('Efekty/Rezultaty')
plt.legend()
plt.grid(True)

plt.savefig('zaleznosc_czas_efekt.png')
plt.show()

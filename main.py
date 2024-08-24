import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0, 100, 1000)

x = np.sin(a) + 0.5 * a

plt.plot(a, x)
plt.xlabel("Abcissa")
plt.ylabel("Coordenada")
plt.title("Caralho")
plt.show()
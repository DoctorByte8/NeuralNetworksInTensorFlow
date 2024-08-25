import numpy as np
import matplotlib.pyplot as plt

x = np.random.random(10000)

plt.scatter(x[:5000], x[5001:])

plt.show()
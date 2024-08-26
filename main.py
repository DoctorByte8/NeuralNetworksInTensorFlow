import numpy as np
import matplotlib.pyplot as plt

# Generate the array with random values between -1 and 1
arr = np.random.random((1000, 2))
arr = (arr * 2) - 1

# Create an array for colors based on conditions:
# - If both x and y are positive or both are negative, color = 1 (e.g., blue)
# - If one is positive and the other is negative, color = 0 (e.g., red)

colors = np.where((arr[:, 0] > 0) & (arr[:, 1] > 0) | (arr[:, 0] < 0) & (arr[:, 1] < 0), 1, 0)

# Create a scatter plot using the color array
plt.scatter(arr[:, 0], arr[:, 1], c=colors, cmap='bwr')  # 'bwr' colormap for red/blue
plt.show()

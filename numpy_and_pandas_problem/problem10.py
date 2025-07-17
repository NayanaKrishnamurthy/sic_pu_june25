import numpy as np
import matplotlib.pyplot as plt
data = np.random.randn(1000)

# Create histogram with 30 bins
plt.hist(data, bins=30, color='green', edgecolor='black')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()
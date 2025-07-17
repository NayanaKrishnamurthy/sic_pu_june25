import matplotlib.pyplot as plt
import seaborn as sns
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

# Create bar chart
plt.bar(categories, values, color=['blue', 'green', 'red', 'purple'])
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart")
plt.show()
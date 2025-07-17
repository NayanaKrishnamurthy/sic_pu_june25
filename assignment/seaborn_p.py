import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample dataset
data = sns.load_dataset('tips')

# Scatter plot with regression line
sns.lmplot(x='total_bill', y='tip', data=data, hue='sex', markers=['o', 's'])
plt.title('Total Bill vs Tip')
plt.show()

# Box plot
sns.boxplot(x='day', y='total_bill', data=data, palette='coolwarm')
plt.title('Total Bill Distribution by Day')
plt.show()

# In a np array of spendings of the week, find the highest spending and the day.


import numpy as np

week_spendings = np.array([50, 120, 30, 40, 200, 90, 300])
index = np.argmax(week_spendings)
big_spending = week_spendings[index]

days = {0:'mon', 1:'tue', 2:'wed', 3:'thu', 4:'fri', 5:'sat', 6:'sun'}

print(f"Highest spending: {big_spending} on {days[index]}")

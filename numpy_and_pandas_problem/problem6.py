import math
import numpy as np

user_number = int(input('Enter a number of your choice between [0 and 9]: '))
system_number = np.random.randint(10)
if system_number == user_number:
	print('CrorePati')
else:
	print('RoadPati')
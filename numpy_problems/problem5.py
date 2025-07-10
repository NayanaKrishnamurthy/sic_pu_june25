import numpy as np

arr = np.arange(1, 10)
print(arr, '\n')

# Reshape to 3x3 matrix
arr = arr.reshape(3, 3)
print(arr, '\n')

# Reshape back to the original size
arr = arr.reshape(9) # generates 1D array
print(arr)

arr = arr.reshape(1, 9) # generates 2D array
print(arr)

arr=arr.reshape(3,-1)  # row =3,column = num of element in lis / row =  9/3=3
print(arr)

arr=arr.reshape(-1,3) # row = 9/3 = 3
print(arr)

arr=arr.reshape(-1,-1)  # error
#arr = arr.reshape(2, 5) # ValueError

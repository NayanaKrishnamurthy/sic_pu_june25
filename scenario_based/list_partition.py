n=8
x=3
y=5
N=[2,4,9,4,42,24,33,12]
N.sort(reverse=True)
print(f'sorted list is {N}')
p=N[x-1]-N[x]-1
print(f'number of element between x[i]>p and y[i]<p is {p}')
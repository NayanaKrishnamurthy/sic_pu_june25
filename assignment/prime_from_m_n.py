
m = int(input("Enter m (smaller number): "))
n = int(input("Enter n (larger number): "))

for i in range(n - 1, m, -1):
    if i < 2:
        continue  

    is_prime = True

    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        print(i, end=' ')

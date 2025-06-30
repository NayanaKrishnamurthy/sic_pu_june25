n = int(input("Enter an odd number for the square size: "))
if n % 2 == 0:
    print("Please enter an odd number.")
else:
    for i in range(n):
        for j in range(n):
            is_border = i == 0 or i == n - 1 or j == 0 or j == n - 1
            is_diagonal = j == i or j == n - 1 - i
            is_center = i == j == n // 2
            if is_center:
                print("0", end="")
            elif is_border or is_diagonal:
                print("*", end="")
            else:
                print(" ", end="")
        print()

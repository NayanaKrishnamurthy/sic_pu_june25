lines = int(input("B. Enter number of lines for Equilateral Triangle: "))

for i in range(lines):
    print(' ' * (lines - i - 1) + '*' * (2 * i + 1))

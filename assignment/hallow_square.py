lines = int(input("C. Enter number of lines for Hollow Square: "))

for i in range(lines):
    for j in range(lines):
        if i == 0 or i == lines - 1 or j == 0 or j == lines - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()


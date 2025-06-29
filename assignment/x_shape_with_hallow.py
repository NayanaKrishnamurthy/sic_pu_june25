lines = int(input("G. Enter number of lines for Hollow Square with X and 0 at Center: "))

for i in range(lines):
    for j in range(lines):
        if i == 0 or i == lines - 1 or j == 0 or j == lines - 1:
            print('*', end='')
        elif i == j or i + j == lines - 1:
            if lines % 2 == 1 and i == lines // 2 and j == lines // 2:
                print('0', end='')
            else:
                print('*', end='')
        else:
            print(' ', end='')
    print()

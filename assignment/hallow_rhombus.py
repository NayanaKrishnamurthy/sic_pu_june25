lines = int(input(" Enter number of lines for Hollow Rhombus: "))

for i in range(lines):
    print(' ' * (lines - i - 1), end='')
    for j in range(lines):
        if i == 0 or i == lines - 1 or j == 0 or j == lines - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

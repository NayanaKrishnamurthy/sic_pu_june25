lines = int(input("E. Enter number of lines for Pascal's Triangle: "))

for i in range(lines):
    print(' ' * (lines - i), end='')
    val = 1
    for j in range(i + 1):
        print(val, end=' ')
        val = val * (i - j) // (j + 1)
    print()

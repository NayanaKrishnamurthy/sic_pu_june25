
n = input("Enter a number: ")
count = 0

for ch in n:
    if ch == '2' or ch == '3' or ch == '5' or ch == '7':
        count = count + 1

print("Number of prime digits:", count)

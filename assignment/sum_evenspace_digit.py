## even space ##
n = input("Enter the number: ")
sum = 0

for i in range(len(n)):
    if i % 2 == 0:  
        sum += int(n[i])

print(f'Sum of digits at even positions is {sum}')


## odd space ##
n = input("Enter the number: ")
sum = 0

for i in range(len(n)):
    if i % 2 == 0:  # Even index (0, 2, 4, ...)
        sum += int(n[i])

print(f'Sum of digits at even positions is {sum}')


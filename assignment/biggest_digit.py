
number = int(input("Enter a number: "))
number = abs(number)  

max_digit = 0

for digit in str(number):
    if int(digit) > max_digit:
        max_digit = int(digit)

print("Biggest digit:", max_digit)

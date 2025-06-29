n = input("Enter the number: ")

# Convert to a list of digits
digits = []

for ch in n:
    if ch.isdigit():
        digits.append(ch)

# Remove duplicates and sort
digits = list(set(digits))
digits.sort()

# Check and print result
if len(digits) < 2:
    print("No second smallest digit")
else:
    print("Second smallest digit is", digits[1])


n = input("Enter the number: ")
digits = []

for ch in n:
    if ch.isdigit():
        digits.append(ch)

digits = list(set(digits))
digits.sort()

if len(digits) < 2:
    print("No second smallest digit")
else:
    print("Second smallest digit is", digits[1])


n = int(input('Enter N (term) value: '))
m = int(input('Enter number of terms: '))

sum_of_series = 0
sign = -1

for i in range(m):
    numerator   = n ** (2 ** i)
    denominator = 2 * i + 1
    sign        = sign * -1
    term        = (numerator / denominator) * sign
    sum_of_series = sum_of_series + term

print("Sum of the series is:", sum_of_series)

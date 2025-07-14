from collections import Counter

arr = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
brr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]

# Count frequency of elements in both lists
count_arr = Counter(arr)
count_brr = Counter(brr)

# Find missing elements (where frequency in brr > arr)
missing = []

for num in count_brr:
    if count_brr[num] > count_arr.get(num, 0):
        missing.append(num)

# Sort and print missing numbers
missing.sort()
print("Missing numbers:", ' '.join(map(str, missing)))

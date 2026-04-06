numbers = [9, 41, 12, 3, 74, 91]

largest = None

for num in numbers:
    if largest is None:
        largest = num
    elif num > largest:
        largest = num

print(largest)
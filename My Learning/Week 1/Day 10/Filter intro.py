# Filter intro
print()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = list(filter(lambda s: s % 2 == 0, numbers))
print(even)

above_five = list(filter(lambda s: s > 5, numbers))
print(above_five)

print()
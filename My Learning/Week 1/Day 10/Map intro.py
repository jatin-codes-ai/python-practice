# map intro
print()

# map() returns map object so wrap it with a list() to see results
numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda m: m ** 2, numbers))
print(squared)

string = list(map(str, numbers))
print(string)

print()
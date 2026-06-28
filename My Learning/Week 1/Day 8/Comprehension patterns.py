# Comprehension patterns
print()

# 1. list of students report
students = [
    ("Jatin",[89, 98, 87]),
    ("Neeraj",[78,67,87]),
    ("Bhavishya",[88, 78, 96])
]
averages = {name: round(sum(marks)/len(marks), 2) for name, marks in students}
print(f"Results: {averages}")

# 2. Tuple unpacking in comprehension
data = [('a', 1), ('b', 2), ('c', 3)]
result = []
for item in data : # old way 
    letter, number = item
    result.append(letter * number)

result = [letter * number for letter, number in data ] # comprehension way
print(f"Results: {result}")

# 3. Nested list comprehension
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(f"Flat: {flat}")

# 4. If-else comprehension
numbers = [1, 2, 3, 4, 5]

even = [x for x in numbers if x%2 == 0]

print(f"Even: {even}")

label = ["even" if x % 2 == 0 else "odd" for x in numbers]

print(f"Labels: {label}")

print()
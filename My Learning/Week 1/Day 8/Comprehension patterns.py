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
# result = []
# for item in data : # old way 
#     letter, number = item
#     result.append(letter * number)

result = [letter * number for letter, number in data ] # comprehension way
print(f"Results: {result}")

print()
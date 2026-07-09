# Lambda applications

print()
print("=== Lambda applications ===")

# Students records
students = [
    {"name": "Jatin", "age": 23, "marks": 93},
    {"name": "Bhavishya", "age": 21, "marks": 91},
    {"name": "Neeraj", "age": 23, "marks": 87}
]
#1. ascending marks sorting
inc_marks = sorted(students, key = lambda s:s["marks"])
print("\nSorted by increasing marks - ")
for s in inc_marks:
    print(f"    {s['name']}: {s['marks']}")

#2. descending marks sorting
dec_marks = sorted(students, key = lambda s:s["marks"], reverse= True)
print("\nSorted by decreasing marks - ")
for s in dec_marks:
    print(f"    {s['name']}: {s['marks']}")

# 3. by name sorting
by_name = sorted(students, key = lambda s :s["name"])
print("\nName sorting -")
for s in by_name:
    print(f"    {s['name']}")

# 4. age then marks sorting
age_marks = sorted(students, key = lambda s: (s["age"], s["marks"]))
print("\nAge-Marks sorting -")
for s in age_marks:
    print(f"    {s['name']}: Age {s['age']}, Marks {s['marks']}")

# 5. Using lambda with list comprehension
get_name = lambda student: student["name"]
names = [get_name(s) for s in students]
print("\nAll names -")
print(names)

# 6. Grade assigner
assign_grade = lambda marks: (
    "A+" if marks >= 90 else
    "A"  if marks >= 80 else
    "B"  if marks >= 70 else
    "C"  if marks >= 60 else
    "D"  if marks >= 50 else
    "F"
)
print("\nGrade Report - ")
for s in students:
    grade = assign_grade(s["marks"])
    print(f"    {s['name']}: {s['marks']} - Grade {grade}")

# 7. Topper
topper = max(students, key = lambda s: s["marks"])
lowest = min(students, key = lambda s: s["marks"])
print(f"\nTopper: {topper['name']} with {topper['marks']} marks")
print(f"Needs improvement: {lowest['name']} with {lowest['marks']} marks")

# 8. Average
total = sum(map(lambda s: s["marks"], students))
average = total/len(students)
print(f"\nClass avearge: {average:.1f}")

#9. Sorter factory
def make_sorter(key):
    return lambda student: student[key]
print("\nSorter factory -")
age_sort = make_sorter("age")
youngest_first = sorted(students, key = age_sort)
for s in youngest_first:
    print(f"    {s['name']}: Age {s['age']}")

print()
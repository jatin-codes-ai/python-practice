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
print("Sorted by increasing marks - ")
for s in inc_marks:
    print(f"{s['name']}: {s['marks']}")
#2. descending marks sorting
dec_marks = sorted(students, key = lambda s:s["marks"], reverse= True)
print("Sorted by decreasing marks - ")
for s in dec_marks:
    print(f"{s['name']}: {s['marks']}")

print()
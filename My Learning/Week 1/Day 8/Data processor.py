# Data processor

print()

print("=== Data Processor ===")
record = [
    ("Jatin", [85, 90, 95]),
    ("Neeraj", [81, 78, 60]),
    ("Bhavishya", [89, 88, 78])
    ]
# 1
students = [name for name, marks in record]
print(f"All students: {students}")
# 2
averages = {name: round(sum(marks)/len(marks), 2) for name, marks in record}
print(f"\nAverages:")
for name, avg in averages.items():
    print(f"  {name}: {avg}")
# 3
distinction = [name for name, avg in averages.items() if avg >= 75]
print(f"\nDistinction: {distinction}")

# 4
def get_grade(avg):
    if avg >= 90 : return "A+"
    elif avg >= 80 : return "A"
    elif avg >= 70 : return "B"
    elif avg >= 60 : return "C"
    elif avg >= 50 : return "D"
    else : return "F"
grades = {name: get_grade(avg) for name, avg in averages.items()}
print("\nGrades:")
for name, grade in grades.items():
    print(f"{name}: {grade} Grade")
# 5
all_marks = [marks for name,row in record for marks in row]
print(f"All marks: {all_marks}")
# 6
above_80 = [marks for marks in all_marks if marks > 80]
print(f"Marks above 80: {above_80}")

print()
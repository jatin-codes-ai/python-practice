# Data processor

print()

print("=== Data Processor ===")
record = [
    ("Jatin", [85, 90, 95]),
    ("Neeraj", [81, 78, 60]),
    ("Bhavishya", [89, 88, 78])
    ]

students = [name for name, marks in record]
print(f"All students: {students}")

averages = {name: round(sum(marks)/len(marks), 2) for name, marks in record}
print(f"\nAverages:")
for name, avg in averages.items():
    print(f"  {name}: {avg}")

distinction = [name for name, avg in averages.items() if avg >= 75]
print(f"\nDistinction: {distinction}")



print()
# Student analyzer
print()

print("=" * 55)
print("   STUDENT PERFORMANCE ANALYZER")
print("=" * 55)

students = [
    {"name": "Jatin", "age": 23, "marks": 95, "city": "Delhi"},
    {"name": "Bhavishya", "age": 21, "marks": 65, "city": "Rajasthan"},
    {"name": "Neeraj", "age": 23, "marks": 36, "city": "Bihar"},
    {"name": "Vashu", "age": 21, "marks": 28, "city": "Mumbai"}
]

all_names = list(map(lambda s: s["name"], students))
print(f"All students: {all_names}")

all_marks = list(map(lambda s: s["marks"], students))
print(f"All marks: {all_marks}")

def get_grade(marks):
    if marks >= 90: return "A+"
    elif marks >= 80: return "A"
    elif marks >= 70: return "B"
    elif marks >= 60: return "C"
    elif marks >= 40: return "D"
    else: return "F"

graded = list(map(lambda m:{**m, "grade": get_grade(m["marks"])}, students))
# print(f"Grades: {graded}")
print("\nGRADE REPORT: ")
for s in graded:
    bar = "█" * (s["marks"] // 10)
    print(f"  {s['name']:<10} {s['marks']:>3}  {bar:<10} Grade: {s['grade']}")

print("\n━━━ FILTERED LISTS ━━━")

# Students who passed
passed = list(filter(lambda s: s["marks"] >= 40, students))
failed = list(filter(lambda s: s["marks"] < 40, students))

passed_names = list(map(lambda s: s["name"], passed))
failed_names = list(map(lambda s: s["name"], failed))

print(f"\nPassed ({len(passed)}): {passed_names}")
print(f"Failed ({len(failed)}): {failed_names}")

# Distinction holders
distinction = list(filter(lambda s: s["marks"] >= 75, students))
dist_names  = list(map(lambda s: f"{s['name']}({s['marks']})", distinction))
print(f"\nDistinction: {dist_names}")

# Students from Mumbai
mumbai = list(filter(lambda s: s["city"] == "Mumbai", students))
mumbai_names = list(map(lambda s: s["name"], mumbai))
print(f"\nFrom Mumbai: {mumbai_names}")

# Students above age 21
mature = list(filter(lambda s: s["age"] > 21, students))
mature_info = list(map(lambda s: f"{s['name']}(Age:{s['age']})", mature))
print(f"Age > 21:    {mature_info}")

print("\n━━━ CLASS STATISTICS ━━━")

marks_list = list(map(lambda s: s["marks"], students))

total   = sum(marks_list)
average = total / len(marks_list)
highest = max(marks_list)
lowest  = min(marks_list)

topper  = list(filter(lambda s: s["marks"] == highest, students))[0]
weakest = list(filter(lambda s: s["marks"] == lowest,  students))[0]

print(f"\nTotal Students:  {len(students)}")
print(f"Class Average:   {average:.1f}")
print(f"Highest Marks:   {highest} — {topper['name']}")
print(f"Lowest Marks:    {lowest} — {weakest['name']}")
print(f"Pass Rate:       {len(passed)}/{len(students)} "
      f"({len(passed)/len(students)*100:.0f}%)")

print("\n━━━ BONUS MARKS FOR FAILED STUDENTS ━━━")
print("(Policy: Failed students get +10 bonus, capped at 40)")

adjusted = list(map(
    lambda s: {**s, "marks": min(s["marks"] + 10, 40)}
    if s["marks"] < 40 else s,
    students
))

still_failed = list(filter(lambda s: s["marks"] < 40, adjusted))
now_passed   = list(filter(
    lambda s: s["marks"] >= 40,
    [a for a in adjusted if a not in
     list(filter(lambda o: o["marks"] >= 40, students))]
))

for s in adjusted:
    original = list(filter(
        lambda o: o["name"] == s["name"], students))[0]
    if original["marks"] < 40:
        print(f"  {s['name']}: {original['marks']} → {s['marks']}")

print("\n" + "=" * 55)
print("STUDENT ANALYZER — COMPLETE")
print("=" * 55)

print()
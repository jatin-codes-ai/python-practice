# Student Marks Manager

print()

marks = []
subjects = ['Maths', 'Physics', 'Chemistry', 'English', 'CS']

print("=== STUDENT MARKS MANAGER ===")
print("Enter marks for each subjects out of 100 :\n")

for subject in subjects :
    mark = int(input(f"{subject}: "))
    marks.append(mark)

total = sum(marks)
average = total/len(marks)
highest = max(marks)
lowest = min(marks)

print("\n=== RESULT ===")
print(f"Total: {total}/{len(marks)*100}")
print(f"Average: {average:.2f}")
print(f"Highest mark:\n{subjects[marks.index(highest)]}: {highest}")
print(f"Lowest: {lowest}")

if average >= 75:
    print("Grade: Distinction")
elif average >= 60:
    print("Grade: First Class")
elif average >= 40:
    print("Grade: Pass")
else:
    print("Grade: Fail")

print()
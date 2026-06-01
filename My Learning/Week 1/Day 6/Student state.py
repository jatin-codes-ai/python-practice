# Student state 

print ()

def calculate_stats(marks_list):
    highest = max(marks_list)
    lowest = min(marks_list)
    total = sum(marks_list)
    average = total/len(marks_list)

    return (highest, lowest, average, total)

print ("STUDENT MARKS CALCULATOR")
print()
print("Enter 5 marks: ")
marks_list = []

for i in range(1,6) :
    marks = int(input(f"Mark {i}: "))
    marks_list.append(marks)

print()


print("Student stats: ")

highest, lowest, average, total = calculate_stats(marks_list)

print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Average: {average}")
print(f"Total: {total}")

print()
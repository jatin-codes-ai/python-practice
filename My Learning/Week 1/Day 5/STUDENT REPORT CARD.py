# STUDENT REPORT CARD

print()

students = {
    "Jatin Kumar": {
        'age': 23,
        'marks': [70, 86, 64, 71, 77],
        'city': 'Delhi'
    },
    "Neeraj": {
        'age': 22,
        'marks': [54, 45, 78, 64, 57],
        'city': 'Mumbai'
    },
    "Bhavishya Rathi": {
        'age': 20,
        'marks': [89, 78, 87, 77, 65],
        'city': 'Delhi'
    }
}

def get_average(student_name):
    marks_list = students[student_name]['marks']
    return sum(marks_list) / len(marks_list)

while True :
    print("\n=== STUDENT REPORT CARD ===")

    print("1. Show all students\n" \
    "2. Show one student's report\n" \
    "3. Show class average\n" \
    "4. Exit \n")
    ip = int(input("Enter your option: "))

    if not (1 <= ip <= 4) :
        print('Invalid option.\n')

    elif ip == 1 :
        print("All Students: ")
        
        for i, (key , value) in enumerate(students.items(), start = 1) :
            average_marks = get_average(key)
            print(f"{i}. {key} \n   City: {students[key]['city']}\n   Average: {average_marks} ")
            
        print()

    elif ip == 2 :
        print("Individual Student's Report: ")
        name = input("Enter the name: ").title()
        if name in students.keys() :
            for key, value in students[name].items() :
                print(f"{key}: {value}")
            total_marks = sum(students[name]['marks'])
            print(f"Total marks: {total_marks}")
            total_subjects = len(students[name]['marks'])
            print(f"Average: {total_marks/total_subjects}")
        else :
            print("Not found.")
        print()

    elif ip == 3 :
        print("Students Average: ")
        averages = []
        for i, (key , value) in enumerate(students.items(), start= 1) :
            average_marks = get_average(key)
            print(f"{i}. {average_marks}")
            averages.append(average_marks)
            # i += 1
        class_average = sum(averages)/len(averages)
        print(f"Class Average: {class_average}")

    else :
        print("THANK YOU!")
        break

print()
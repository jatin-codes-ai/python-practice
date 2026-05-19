print()
# taking students input 
marks = int(input("Enter marks out of 100: "))

# Grading criteria
if(marks > 100 or marks<0 ):
    print("invalid input")
elif(marks >= 90):
    grade = 'A'
    remarks = 'Excellent'
elif(marks >= 80):
    grade = 'B'
    remarks = 'Very Good'
elif(marks >= 70):
    grade = 'C'
    remarks = 'Good'
elif(marks >= 60):
    grade = 'D'
    remarks = 'Average'
elif(marks >= 40):
    grade = 'E'
    remarks = 'Below Average'
else:
    grade = 'F'
    remarks = 'Failed'

# Results
if(0<= marks <= 100):
    print(f"Your grade is {grade},")
    print(f"Remarks: {remarks}!")



print()
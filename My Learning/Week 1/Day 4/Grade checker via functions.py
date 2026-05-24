# Rebuild Grade checker with functions

print()

print("===== GRADE CHECKER =====")

marks = int(input("Enter your marks: "))



def grade(marks) :

    if marks in range(0, 101) :


        if marks >= 90 :
            return 'Grade A+'
        elif marks >= 80 :
            return 'Grade A'
        elif marks >= 70 :
            return 'Grade B'
        elif marks >= 60 :
            return 'Grade C'
        elif marks >= 40 :
            return 'Grade D'
        return 'Grade F'

    
    return 'Invalid marks' 
    
print(grade(marks))

print("="*25)
print()
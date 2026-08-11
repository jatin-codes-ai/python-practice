# Rebuild Grade checker with functions

print()

print("===== GRADE CHECKER =====")

marks = int(input("Enter your marks: "))



def grade(marks) :

    if not ( 0 <= marks <= 100 ) :
        return 'Invalid marks' 

    
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

    
    
print(grade(marks))

print("="*25)
print()
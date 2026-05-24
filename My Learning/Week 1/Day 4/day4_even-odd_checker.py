# Even/odd checker

print()

# Title name
print("=== Even/Odd Checker ===")

# Even/odd logic
def is_even(number):
    if number % 2 == 0 :
        return True
    return False

# list of numbers
numbers = [1, 3, 4, 34, 345, 64, 765, 23, 5343, 224]

# looping on list 
if len(numbers) :
    
    # function call
    for number in numbers :
        if is_even(number) == True :
            print(f"{number} is even.")
        else: 
            print(f"{number} is odd.")



# Ending        
print('='*24)

print()
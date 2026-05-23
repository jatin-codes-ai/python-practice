# day4_calculator with functions

print()

print("="*20, "SMART CALCULATOR" , "="*20)

# functions
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b 
def multiply(a, b):
    return a * b 
def divide(a, b):
    if b == 0 :
        return "--Cannot be divided by zero."
    # no need for else
    return a / b

lasts = []


while True :

    print("\n1. Calculate     2. Show all result     3. Exit")
      
    ip = input("\nChoose any one option: ")

    # Calculation performance
    if ip == '1' :
    
        # inputs
        a = float(input("Enter 1st number : "))
        b = float(input("Enter 2nd number : "))

        # ask for operation
        operation = input("\nChoose your operation carefully (+, -, *, /): ")

        # processing
        if operation == '+' :
            result = add(a, b)
        elif operation == '-' :
            result = subtract(a, b)
        elif operation == '*' :
            result = multiply(a, b)
        elif operation == '/' :
            result = divide(a, b)
        # defense
        else :
            result = "--Invalid operation. Choose any one of the given above."

        lasts.append(result)
        # output
        print(f"\nResult : {result}")

    # History

    elif ip == '2' :
        print("\nAll results: ")
        if len(lasts) == 0 :
            print("No previous results exist.")
        else :
            i = 1
            # print(lasts)
            for last in lasts :
                print(f"{i}. {lasts[i-1]} ")
                i += 1
            print(f"Total number of results: {len(lasts)}")
    
    # Exiting the app 
    elif ip == '3' :
          print("\nExiting the program.\nThank you, User!")
          break
    
    # Main defense line
    else :
        print("Choose any from 1, 2 or 3.\n")
    
print()
print("="*27, "END" , "="*27)

print()
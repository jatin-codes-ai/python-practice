
# safe_calculator.py

print()
print("=" * 40)
print("         SAFE CALCULATOR — v1")
print("=" * 40)

def get_number(prompt):
    
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Not a valid number. Try again.")

def do_add(a, b):
    return a + b

def do_subtract(a, b):
    return a - b

def do_multiply(a, b):
    return a * b

def do_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None


while True:
    print("\nOperations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

    choice = input("\nYour choice: ")

    if choice == "1":
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        result = do_add(num1, num2)
        print(f"Result: {num1} + {num2} = {result}")

    elif choice == "2":
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        result = do_subtract(num1, num2)
        print(f"Result: {num1} - {num2} = {result}")

    elif choice == "3":
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        result = do_multiply(num1, num2)
        print(f"Result: {num1} * {num2} = {result}")

    elif choice == "4":
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        result = do_divide(num1, num2)
        if result is not None:
            print(f"Result: {num1} / {num2} = {result}")

    elif choice == "5":
        print("\nGoodbye! Thanks for calculating safely.")
        break

    else:
        print("Invalid choice. Please pick 1-5.")


print("=" * 40)
print()
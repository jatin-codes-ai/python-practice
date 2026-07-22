# error_basics.py

print()
print("=" * 40)
print("         ERROR HANDLING BASICS")
print("=" * 40)

# ------ DEMO 1: Bare try/except ------
print("\n--- DEMO 1: Bare try/except ---")
print("Trying to convert 'hello' to int...")
try:
    int("hello")
except:
    print("Something went wrong! But program didn't crash.")

# ------ DEMO 2: Catching ValueError specifically ------
print("\n--- DEMO 2: Catching ValueError ---")
print("Trying to convert 'python' to int...")
try:
    int("python")
except ValueError:
    print("Caught ValueError: That wasn't a valid number.")

# ------ DEMO 3: Catching ZeroDivisionError ------
print("\n--- DEMO 3: Catching ZeroDivisionError ---")
print("Trying: 100 / 0")
try:
    result = 100 / 0
except ZeroDivisionError:
    print("Caught: Cannot divide by zero!")

# ------ DEMO 4: Catching FileNotFoundError ------
print("\n--- DEMO 4: Catching FileNotFoundError ---")
print("Trying to open 'nonexistent.txt'...")
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Caught: File does not exist.")

# ------ DEMO 5: Multiple except blocks in one try ------
print("\n--- DEMO 5: Multiple except blocks ---")
try:
    num = int(input("Enter a number to divide 100 by: "))
    result = 100 / num
    print(f"Result: {result}")
except ValueError:
    print("That's not a number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# ------ DEMO 6: Using 'as e' to see the error message ------
print("\n--- DEMO 6: Using 'as e' to see error message ---")
print("Trying to convert 'abc' to int...")
try:
    int("abc")
except ValueError as e:
    print(f"Full error message: {e}")

# ------ DEMO 7: try/except/else ------
print("\n--- DEMO 7: try/except/else ---")
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That's not a number!")
else:
    print(f"No error! You entered {num}. Squared = {num**2}.")

# ------ FOOTER ------
print()
print("=" * 40)
print("         DAY 13 COMPLETE")
print("=" * 40)
print()
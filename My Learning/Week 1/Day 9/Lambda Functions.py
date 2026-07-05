# Lambda Functions

print("=" * 50)
print("LAMBDA FUNCTIONS — BASICS")
print("=" * 50)

# 1. Basic lambda
square = lambda x: x * x
cube = lambda x: x ** 3
double = lambda x: x * 2

print("\n--- MATH LAMBDAS ---")
print(f"Square of 7: {square(7)}")
print(f"Cube of 4: {cube(4)}")
print(f"Double of 15: {double(15)}")

# 2. Multi-argument lambda
add = lambda x, y: x + y
multiply = lambda x, y: x * y
power = lambda base, exp: base ** exp

print("\n--- TWO-ARGUMENT LAMBDAS ---")
print(f"Add 8 + 12: {add(8, 12)}")
print(f"Multiply 6 × 7: {multiply(6, 7)}")
print(f"Power 2^10: {power(2, 10)}")

# 3. Lambda with string
greet = lambda name: f"Rise, {name}. The arc continues."
shout = lambda text: text.upper() + "!!!"
reverse = lambda text: text[::-1]

print("\n--- STRING LAMBDAS ---")
print(greet("Jatin"))
print(shout("sealed awakener"))
print(f"Reversed 'ascension': {reverse('ascension')}")

# 4. Lambda with condition (ternary)
# lambda x: value_if_true if condition else value_if_false
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
grade = lambda score: "Pass" if score >= 40 else "Fail"
category = lambda age: "Minor" if age < 18 else "Adult"

print("\n--- CONDITIONAL LAMBDAS ---")
print(f"Is 7 even? {is_even(7)}")
print(f"Is 12 even? {is_even(12)}")
print(f"Score 35: {grade(35)}")
print(f"Score 67: {grade(67)}")
print(f"Age 15: {category(15)}")
print(f"Age 23: {category(23)}")

# 5. Lambda in a list (function list)
operations = [
    lambda x: x + 10,
    lambda x: x * 2,
    lambda x: x ** 2,
    lambda x: x - 5
]
op_names = ["Add 10", "Multiply 2", "Square", "Subtract 5"]

print("\n--- FUNCTION LIST ---")
number = 8
for op, name in zip(operations, op_names):
    print(f"{name} applied to {number}: {op(number)}")

# 6. Immediately Invoked Lambda
# You can call a lambda the moment you define it
result = (lambda x, y: x * y + 100)(5, 6)
print(f"\nImmediate invoke (5×6)+100: {result}")

print("\n" + "=" * 50)
print("LAMBDA BASICS COMPLETE")
print("=" * 50)
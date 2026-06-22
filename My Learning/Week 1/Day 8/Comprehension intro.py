# Comprehension intro
print()
print("=== LIST COMPREHENSIONS ===\n")

# 1. Squares 1 to 10
squares = [x*x for x in range(1,11)]
print(f"Squares: {squares}")

# 2. Even from 1 to 30
even = [x for x in range(1,31) if x%2 == 0]
print(f"Even: {even}")

# 3. Uppercase transform
manhwa = ['solo levelling', 'tbate', 'lookism', 'omniscient reader']
upper = [name.upper() for name in manhwa]
print(f"Upper: {upper}")

# 4. length of each
length = [len(name) for name in manhwa]
print(f"Length: {length}")

# 5. Filter + transform
long_title = [name.title() for name in manhwa if len(name) > 6]
print(f"Long titles: {long_title}")

print()
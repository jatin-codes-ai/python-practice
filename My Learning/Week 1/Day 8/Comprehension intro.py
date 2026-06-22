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

# 6. Math on existing list
prices = [100, 200, 300, 400]
with_tax = [round(p * 1.18, 2) for p in prices]
print(f"With tax: {with_tax}")

print("\n=== DICT COMPREHENSIONS ===\n")

skills = ['Python', 'sets', 'tuples', 'functions']
skill_dict = {skill: 'C+' for skill in skills}
print(f"Skills: {skill_dict}")

# 9. From two lists using zip
names = ["Jatin", "Ravi", "Amit"]
ages = [23, 24, 22]
people = {name: age for name, age in zip(names, ages)}
print(f"People: {people}")

print("\n=== SET COMPREHENSIONS ===\n")

# 10. Unique vowels in a string
sentence = "the sealed awakener rises"
vowels = {char for char in sentence if char in "aeiou"}
print(f"Vowels found: {vowels}")

# 11. Unique word lengths
words = ["python", "code", "data", "ml", "ai"]
unique_lengths = {len(w) for w in words}
print(f"Unique word lengths: {unique_lengths}")

print()
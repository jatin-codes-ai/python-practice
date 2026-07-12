# map_filter_basics
print()

# ─── MAP() SECTION ──────────────────────────────────────

print("\n━━━ MAP() — TRANSFORM EVERY ITEM ━━━")

# 1. String transformations
names = ['jatin', 'bhavishya', 'neeraj']

uppercased = list(map(str.upper, names))
capitalized = list(map(str.capitalize, names))
length = list(map(len, names))
rank = list(map(lambda n: f"[D-rank] {n.capitalize()}", names))

print(f"\nNames:       {names}")
print(f"Uppercased:  {uppercased}")
print(f"Capitalized: {capitalized}")
print(f"Lengths:     {length}")
print(f"With Rank:   {rank}")

# 2. Temperature conversion
celsius = [0, 3, 200, 100, 450]
fahrenheit = list(map(lambda c: round((c * 9/5) + 32, 1), celsius))
kelvin = list(map(lambda c: c + 273.15, celsius))

print(f"\nCelsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")
print(f"Kelvin: {kelvin}")

# 3. Map() with two lists
prices = [100, 300, 80, 450, 6200]
discounts = [10, 15, 20, 40, 25]

final_prices = list(map(
    lambda p, d: round(p - (p * d/100), 2), prices, discounts
))

print(f"\nPrices:       {prices}")
print(f"Discounts %:  {discounts}")
print(f"Final Prices: {final_prices}")

# ─── FILTER() SECTION ────────────────────────────────────

print("\n━━━ FILTER() — KEEP ONLY WHAT PASSES ━━━")

# 1. Marks filter
marks = [10, 45, 33, 67, 87, 57, 98, 77, 100, ]
passed = list(filter(lambda m: m >= 40, marks))
failed = list(filter(lambda m: m < 40, marks))
distinction = list(filter(lambda m: m >= 75, marks))

print(f"\nAll marks: {marks}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Distinction: {distinction}")

# ─── COMBINED: map() + filter() ──────────────────────────

print("\n━━━ COMBINED — MAP + FILTER PIPELINE ━━━")

# 1. add 5 bonus marks then filter passed
raw_marks = [23, 45, 37, 26, 46, 75, 64, 95, 83, 59, 87]
pipeline = list(filter(
    lambda m: m >= 40,
    map(lambda m: m + 5, raw_marks)
))
print(f"\nRaw marks: {raw_marks}")
print(f"Passed + bonus: {pipeline}")

print()
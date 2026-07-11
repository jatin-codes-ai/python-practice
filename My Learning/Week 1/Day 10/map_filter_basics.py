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

print()
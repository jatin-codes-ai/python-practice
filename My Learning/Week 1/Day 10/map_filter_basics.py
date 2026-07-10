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


print()
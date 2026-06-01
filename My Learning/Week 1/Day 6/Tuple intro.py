# Tuple intro
print()

print("My Top 5 Manhwa: ")
manhwa = ('Solo Levelling', 'Omniscient Reader', 'Greatest Estate Developer', 'TBATE', 'Lookism')

print(manhwa)

# tuple is immutable, can't add new items like list
# manhwa.append('monster evoution')
print(f"\nFirst: {manhwa[0]}")
print(f"Last: {manhwa[-1]}")
print(f"Total: {len(manhwa)}")
print()

#  i can do this loop but i don't know in depth how i works here
for i, manhwa_name in enumerate(manhwa, start=1)  :
    print(f"{i}. {manhwa_name}")

print()
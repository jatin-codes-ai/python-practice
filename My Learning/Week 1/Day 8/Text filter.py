#  Text filter
print()

print("=== TEXT FILTER ===")
raw = "the SEALED awakener RisEs aGAin from daRKNEss."
print(f"Raw: {raw}")
print(f"Clean: {raw.lower()}")
print(f"Title: {raw.title()}")

vowels = [v for v in raw.lower() if v in 'aeiou']
print(f"Vowels: {vowels}")
print(f"Vowels count: {len(vowels)}")
constants = [c for c in raw.lower() if c not in 'aeiou. ']
print(f"Constants: {constants}")
print(f"Constant count: {len(constants)}")

words = raw.title().split()
words_length = {word: len(word) for word in words}
print(f"Word Length: {words_length}")
long_word = [word for word in words if len(word) > 4]
print(f"Long words(>4): {long_word}")

reverse = [word.__reversed__() for word in words]
print(f"Reversed: {reverse}")

print()
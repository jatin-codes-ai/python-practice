# Text analyzer
print()

print("TEXT ANALYZER")

text1 = "the quick brown fox jumps over the lazy dog"
text2 = "the slow brown turtle walks under the lazy cat"

word1 = set(text1.split())
word2 = set(text2.split())

print(f"text 1 words: {word1}")
print(f"text 2 words: {word2}")

common = word1 & word2
print(f"Common words: {common}")
print(f"Count: {len(common)}")

unique1 = word1 - word2
print(f"Unique to text 1: {unique1}")
unique2 = word2 - word1
print(f"Unique to text 1: {unique2}")



print()
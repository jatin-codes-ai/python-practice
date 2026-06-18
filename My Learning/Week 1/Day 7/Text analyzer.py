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

all_words = word1 | word2
print(f"Total unique words: {len(all_words)}")

similarity = len(common)/len(all_words)
print(f"Similarity score: {similarity:.2%}")

total_words = len(text1.split())
unique_in_text1 = len(word1)
print(f"\nText 1 total words: {total_words}")
print(f"Text 1 unique words: {unique_in_text1}")
print(f"Repetition factor: {total_words - unique_in_text1}")

spam_keywords = {"win", "free", "prize", "click", "buy"}
message = "click here to win a free prize"
message_words = set(message.lower().split())

caught_spam = message_words & spam_keywords
if caught_spam:
    print(f"\nSPAM DETECTED! Triggers: {caught_spam}")
else:
    print(f"\nMessage clean")

print()
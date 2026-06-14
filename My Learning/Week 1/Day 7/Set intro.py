# Set intro 

# print()
# # languages
# languages  = {"Python", "Python", "SQL", "Javascript", "Python"}
# print(f"My languages: {languages}")

# languages.add("Java")
# print(f"After adding Java: {languages}")

# languages.remove("Javascript")
# print(f"After removing Javascript: {languages}")

# print(f"Is Python in set? {'Python' in languages}")

# # visitors list
# visitors = ["jatin", "ravi", "jatin", "amit", "ravi", "jatin"]
# unique_visitors = set(visitors)

# print(f"\nTotal visits: {len(visitors)}")
# print(f"Unique visitors: {len(unique_visitors)}")
# print(f"Unique names: {unique_visitors}")

# # skillset
# my_skills = {"Python", "Capcut", "Calisthenics"}
# needed_for_job = {"Python", "SQL", "ML", "Pandas"}
# already_have = my_skills.intersection(needed_for_job)
# print(f"\nSkills I already have: {already_have}")
# need_to_learn = needed_for_job - my_skills
# print(f"Skills I still need to learn: {need_to_learn}")

# print()


# set methods drill

# Set Methods Practice

print("=== SET METHODS DRILL ===\n")

# Create starting set
languages = {"Python", "Java", "C++"}
print(f"Start: {languages}")

# 1. Add single
languages.add("JavaScript")
print(f"After add JS: {languages}")

# 2. Add multiple at once
languages.update(["Go", "Rust", "Swift"])
print(f"After update: {languages}")

# 3. Safe removal (no error if missing)
languages.discard("Pascal")  # Doesn't exist - no error
languages.discard("Java")    # Exists - removed
print(f"After discard: {languages}")

# 4. Check membership
print(f"\nIs Python in set? {'Python' in languages}")
print(f"Is Java in set? {'Java' in languages}")
print(f"Total languages: {len(languages)}")

# 5. Pop (removes random item)
removed = languages.pop()
print(f"\nRandomly removed: {removed}")
print(f"After pop: {languages}")

# 6. Convert list with duplicates to set
visitor_log = ["jatin", "ravi", "jatin", "amit", "ravi", "jatin"]
unique_visitors = set(visitor_log)
print(f"\nLog had {len(visitor_log)} entries")
print(f"Unique visitors: {len(unique_visitors)}")
print(f"Names: {unique_visitors}")

# 7. String to set (gets unique characters)
word = "programming"
unique_chars = set(word)
print(f"\nUnique chars in '{word}': {unique_chars}")

# 8. Clear
languages.clear()
print(f"\nAfter clear: {languages}")
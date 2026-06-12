# Set intro 

print()
# languages
languages  = {"Python", "Python", "SQL", "Javascript", "Python"}
print(f"My languages: {languages}")

languages.add("Java")
print(f"After adding Java: {languages}")

languages.remove("Javascript")
print(f"After removing Javascript: {languages}")

print(f"Is Python in set? {'Python' in languages}")

# visitors list
visitors = ["jatin", "ravi", "jatin", "amit", "ravi", "jatin"]
unique_visitors = set(visitors)

print(f"\nTotal visits: {len(visitors)}")
print(f"Unique visitors: {len(unique_visitors)}")
print(f"Unique names: {unique_visitors}")

# skillset
my_skills = {"Python", "Capcut", "Calisthenics"}
needed_for_job = {"Python", "SQL", "ML", "Pandas"}
already_have = my_skills.intersection(needed_for_job)
print(f"\nSkills I already have: {already_have}")
need_to_learn = needed_for_job - my_skills
print(f"Skills I still need: {need_to_learn}")

print()
# dict_intro 

print()

person = {
    "name": "Jatin kumar", 
    "age": 24,
    "city": "Delhi",
    "college": "NSUT",
}

# Access
print(person["name"])
print()

# Add
person["skill"] = "Python"
person["hobby"] = "Editing"

# Change/edit
person["age"] = 23

print("===== MY INTRO =====")
for key, value in person.items() :
    print(f"{key}: {value}")

print("="*19)
print()
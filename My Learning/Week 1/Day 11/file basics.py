# file basics
print()

print("=" * 40)
print("         FILE HANDLING BASICS")
print("=" * 40)

print("Writing to file: ")
with open("notes.txt", "w") as file:
    file.write("    Hello!,\n    I am Jatin kumar.,\n    I am learning python now.")

print("3 lines written to notes.txt successfully.")
print("Reading full content: ")
with open("notes.txt", "r") as file:
    content = file.read()
    lines = file.readlines() 
print(content)
print("Reading full content line by line: ")
print(lines)

print()
# file basics v1
print()

print("=" * 40)
print("         FILE HANDLING BASICS v1")
print("=" * 40)
# ---------------------- v1 ---------------------------
print("Writing to file: ")
with open("notes.txt", "w") as file:
    file.write("    Hello!\n    I am Jatin kumar.\n    I am learning python now.")

print("3 lines written to notes.txt successfully.")
print("Reading full content: ")
with open("notes.txt", "r") as file:
    content = file.read()
with open("notes.txt", "r") as file:
    lines = file.readlines() 
print(content)
print("Reading full content line by line: ")
for line in enumerate(lines, start=1):
    print(line)
print("Appending 1 extra line: ")
with open("notes.txt", "a") as file:
    file.write("\n   Day 11 file handling intro complete.")
with open("notes.txt", "r") as file:
    content = file.read()
print(content)
# ----------------------------------------------------



print("=== END ===")
print()
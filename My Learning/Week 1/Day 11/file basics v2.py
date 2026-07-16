# file basics v2
print()

print("=" * 40)
print("         FILE HANDLING BASICS v2")
print("=" * 40)

import os
lines = ["I am trying to think a lot.", "But no matter how much i try i can't think about anything.", "It's just like my mind is stuck at a place.", "I feel there's a big thick wall in my brain and i can't get through it."]
print("\nWriting to file: ")
with open("notes2.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")
print(f"{len(lines)} lines written to notes2.txt successfully.")

print("\nReading file content: ")
with open("notes2.txt", "r") as file:
    content = file.read()
print(content)

print("Reading line by line: ")
with open("notes2.txt", "r") as file:
    for index, line in enumerate(file, start=1):
        print(f"Line {index}: {line.strip()}")

print("\nAppending more lines: ")
more_lines = ["I'm in that stage where all my personalities are clashing with each other.", "At the end, all i can think about is DEPRESSION."]
with open("notes2.txt", "a") as file:   
    for more in more_lines:
        file.write(more + "\n")
    
print(f"{len(more_lines)} lines appended successfully.")

print("\nFull content: ")
with open("notes2.txt", "r") as file:
    for index, line in enumerate(file, start=1):
        print(f"Line {index}: {line.strip()}")

print("\nFile info: ")
print(f"File exists: {os.path.exists("notes2.txt")}")
print(f"File size: {os.path.getsize("notes2.txt")} bytes")
with open("notes2.txt", "r") as file:
    total_lines = len(file.readlines())
print(f"Total lines in file: {total_lines}")

print("=" * 40)
print("         END")
print("=" * 40)
print()
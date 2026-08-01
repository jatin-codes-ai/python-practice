# Cultimate
print()

print("=" * 40)
print("             CULTIMATE")
print("Your Manhwa Recommendation Engine")
print("=" * 40)


def get_input(prompt):

    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Not a valid number, Try again.")

while True:

    print()
    print("Menu:")
    print("1. View entire database")
    print("2. Add new manhwa")
    print("3. Get recommendations")
    print("4. Filter by mood")
    print("5. Exit")

    choice = input("Your choice: ")

    if choice = '1':



print("=" * 40)
print("             END")
print()
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

bigshot = {
    "Title": "I'm a cultivation bigshot",
    "Genre": "Cultivaton, Comedy",
    "Tags": "OP MC, hidden strength",
    "Mood": "Funny, chill",
    "Chapters": "600+",
    "Rating": "8.5",
    "Description": "--MC pretends to be weak while being a secret expert."
}
solo = {
    "Title": "Solo levelling", 
    "Genre": "Action, fantasy",
    "Tags": "OP MC, dark",
    "Mood": "Intense, epic",
    "Chapters": "200+", 
    "Rating": "9.0",
    "Description": "--Weakest hunter becomes strongest through mysterious system."
}

while True:

    print()
    print("Menu:")
    print("1. View entire database")
    print("2. Add new manhwa")
    print("3. Get recommendations")
    print("4. Filter by mood")
    print("5. Exit")

    choice = input("Your choice: ")

    if choice == '1':
        print("=" * 30)
        print("     DATABASE")
        print("=" * 30)
        print(bigshot)





print("=" * 40)
print("             END")
print()
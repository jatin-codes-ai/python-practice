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

database = [
{
    "Title": "I'm a cultivation bigshot",
    "Genre": "Cultivaton, Comedy",
    "Tags": "OP MC, hidden strength",
    "Mood": "Funny, chill",
    "Chapters": "600+",
    "Rating": "8.5",
    "Description": "--MC pretends to be weak while being a secret expert."
},
{
    "Title": "Solo levelling", 
    "Genre": "Action, fantasy",
    "Tags": "OP MC, dark",
    "Mood": "Intense, epic",
    "Chapters": "200+", 
    "Rating": "9.0",
    "Description": "--Weakest hunter becomes strongest through mysterious system."
}
]

def display_manhwa(manhwa, index):
    # for manhwa in manhwa:
        print(f"[{index}] {manhwa['Title']}")
        print(f"    Genre: {(manhwa['Genre'])}")
        print(f"    Tags: {(manhwa['Tags'])}")
        print(f"    Mood: {(manhwa['Mood'])}")
        print(f"    Chapters: {manhwa['Chapters']} | Rating: {manhwa['Rating']}")
        print(f"    --> {manhwa['Description']}")
        print("─" * 40)

def view_db():
    print("-" * 25)
    print(f"    DATABASE({len(database)} titles)")
    print("-" * 25)
    for index, manhwa in enumerate(database, start=1):
        display_manhwa(manhwa, index)


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
        view_db()
        print()
    elif choice == '5':
        print("Exiting Cultivation Compass. Happy reading!")
        break
    else:
        print("Invalid choice. Please pick 1-5.")





print("=" * 40)
print("             END")
print()
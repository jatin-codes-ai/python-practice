# Cultimate
print()

print("=" * 40)
print("             CULTIMATE")
print("Your Manhwa Recommendation Engine")
print("=" * 40)


def add_manhwa():
    print("--- Add new manhwa ---")
    title = input("Title:")
    raw_genre = input("Genre(comma-separated): ")
    genres = [g.strip() for g in raw_genre.split()]
    raw_tags = input("Tags(comma-separated): ")
    tags = [t.strip() for t in raw_tags.split()]
    raw_moods = input("Moods(comma-separated): ")
    moods = [m.strip() for m in raw_moods.split()]
    chapters = input("Chapters: ")
    rating = input("Rating: ")
    description = input("Description: ")

    new_manhwa = {
        "Title": title,
        "Genre": genres,
        "Tags": tags,
        "Moods": moods,
        "Chapters": chapters,
        "Rating": rating,
        "Description": description
    }
    database.append(new_manhwa)

    print(f'\n✓ Added "{title}" to database!')



    
database = [
{
    "Title": "I'm a cultivation bigshot",
    "Genre": ["Cultivaton", "Comedy"],
    "Tags": ["OP MC", "hidden strength"],
    "Mood": ["Funny", "chill"],
    "Chapters": "600+",
    "Rating": "8.5",
    "Description": "--MC pretends to be weak while being a secret expert."
},
{
    "Title": "Solo levelling", 
    "Genre": ["Action", "fantasy"],
    "Tags": ["OP MC", "dark"],
    "Mood": ["Intense", "epic"],
    "Chapters": "200+", 
    "Rating": "9.0",
    "Description": "--Weakest hunter becomes strongest through mysterious system."
}
]

def display_manhwa(manhwa, index):
    print(f"[{index}] {manhwa['Title']}")
    print(f"    Genre: {', '.join(manhwa['Genre'])}")
    print(f"    Tags: {', '.join(manhwa['Tags'])}")
    print(f"    Mood: {', '.join(manhwa['Mood'])}")
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
    elif choice == '2':
        add_manhwa()
    elif choice == '5':
        print("\nExiting Cultimate. Happy reading!")
        break
    else:
        print("Invalid choice. Please pick 1-5.")





print("=" * 40)
print("             END")
print()
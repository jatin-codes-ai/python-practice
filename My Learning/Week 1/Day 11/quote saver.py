# quote saver

print("\n========================================")
print("         QUOTE SAVER — v1")
print("========================================")

while True:
    print('''\n1. Add a new quote
2. View all quotes
3. Count quotes
4. Exit''')
    
    choice = input("\nEnter your choice: ")
    print(f"Your choice: {choice}")

    if choice == "1" :
        quote = input("Enter your quote: ")
        with open("quotes.txt", "a") as file:
            file.write(quote + "\n")
        print("Quote saved!")

    elif choice == "2" :
        print("All Quotes ---")
        with open("quotes.txt", "r") as file:
            for index, quote in enumerate(file, start=1) :
                print(f"Quote {index}. {quote.strip()}")
        print("-" * 15 + "\n")

    elif choice == "3" : 
        with open("quotes.txt", "r") as file:
            total_lines = len(file.readlines())
        print(f"You have saved {total_lines} quotes so far.")

    elif choice == "4" :
        print("Goodbye!")
        break

    else :
        print("Invalid choice, please pick from 1-4.")

print("=" * 45)
print()

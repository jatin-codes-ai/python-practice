# quote saver

print("\n========================================")
print("         QUOTE SAVER — v1")
print("========================================")

import os
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

    elif choice == "2":
        if not os.path.exists("quotes.txt"):
            print("\nNo quotes saved yet. Add one first!")
        else:
            with open("quotes.txt", "r") as file:
                quotes = file.readlines()

            if len(quotes) == 0:
                print("\nFile exists but no quotes yet. Add one!")
            else:
                print("\n--- ALL QUOTES ---")
                for index, quote in enumerate(quotes, start=1):
                    print(f"Quote {index}. {quote.strip()}")
                print("-" * 15)


    elif choice == "3" :
        if not os.path.exists("quotes.txt"):
            print("\nNo quotes saved yet. Add one first!")
        else : 
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

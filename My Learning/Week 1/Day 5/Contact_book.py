# Contact_book

print()

print("===== CONTACT BOOK =====")

contact_book = {}


while True :

    print("1. Add   2. Search   3. Show all     4. Exit")
    ip = int(input("Enter your option: "))

    if not ( 1 <= ip <= 4 ) :
        print("Invalid option.\n")

    elif ip == 1 :
        print("\nADD CONTACT: ")
        name = input("Enter name: ")
        phone = int(input("Enter phone number: "))

        contact_book[name] = phone
        print(f"Contact added, {name}.\n")

    elif ip == 2 : 
        print("\nSEARCH: ")
        name1 = input("Enter name: ")

        if name1 in contact_book :
            print(contact_book[name])
        print("Contact not found.\n")

    elif ip == 3 : 
        print("\nSHOW ALL: ")
        if len(contact_book) :
            for key, value in contact_book.items() :
                print(f"{key}: {value}")
        print("No contacts yet.\n")

    else :
        print("Goodbye!")
        break

print('='*18)
print()
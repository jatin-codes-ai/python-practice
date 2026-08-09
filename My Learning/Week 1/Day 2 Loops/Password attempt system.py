# Password attempt system

print()

# take username and password from user
name1 = input("Enter your username: ")
word1 = input("Enter your password: ")

# login details
name2 = 'admin'
word2 = '1234'

# attempt counts
i = 2

# passing condition
if name1 == name2 and word1 == word2:
    print("\nLogin successfull.")
else:
    print(f"\nUsername or password is not correct.\nOnly {i+1} more attempts left.\n")
    while i >= 0:
        name3 = input("Enter your username: ")
        word3 = input("Enter your password: ")
        if name3 == name2 and word3 == word2:
            print("\nLogin successfull.")
            break
            
        else:
            if i > 0:
                print(f"\nUsername or password is not correct.\nOnly {i} more attempts left.\n")
            else:
                print("\nCome back tomorrow.\n")
            i -= 1
        


print()
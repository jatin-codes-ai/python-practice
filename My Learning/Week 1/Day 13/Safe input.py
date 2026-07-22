
# try/except 
print()
print("1. Safe integer input ---")
while True:
    try:
        number = int(input("Enter any number: "))
        print(f"You entered {number}.")
        break
    except ValueError:
        print(f"{number} is not a valid number. Try again.")



print()
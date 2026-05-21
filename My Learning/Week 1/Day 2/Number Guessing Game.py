# Number Guessing Game
# 1st game

print()

import random
secret_number = random.randint(1,10)
attempts = 1
max_attempts = 3

print(f"===== NUMBER GUESSING GAME =====")
print(f"\nI am thinking of a number between 1 to 10.")
print(f"You have {max_attempts} attempts to guess it.")



while attempts <= max_attempts  :

    num1 = int(input("\nEnter Your Guess1: "))

    if num1 == secret_number:
        print(f"\nCongratulations! You have guessed the right number in the {attempts} attenpt.\n")
        break

    elif num1 > secret_number:
        print(f"Too High! You have {max_attempts-attempts} attempts left. ")
        

    elif num1 < secret_number:
        print(f"Too Low! You have {max_attempts-attempts} attempts left. ")
       

    else:
        print(f"Invalid input.You have {max_attempts-attempts} attempts left. ")

    if attempts == 3 :
        print(f"\nGame over. My number was {secret_number}.")
    attempts += 1 
    
print()



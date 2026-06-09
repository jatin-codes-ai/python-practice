# Treasure hunt game
print()
treasures = [(2,3),(5,7),(4,8),(1,9),(6,5)]
print("TREASURE HUNT - 5 treasures hidden!")
print("Guess Coordinates (0-10 range)")
found = []

for attempt in range(1,6):
    print(f"\nAttempt {attempt}/5")
    x = int(input("Enter X: "))
    y = int(input("Enter Y: "))
    guess = (x,y)

    if guess in found:
        print("Already obtained treasure.")
    else:
        for treasure in treasures :
            distance = abs(x - treasure[0]) + abs(y - treasure[0])
            if guess in treasures :
                found.append(guess)
                print(f"Treasure found at {guess}! found: {len(found)}/5")

            elif distance <= 2 : 
                print("Close.")
            else: 
                print("Cold.")

print(f"\nGame Over!\n Total score: {len(found)}/5. ")

print()
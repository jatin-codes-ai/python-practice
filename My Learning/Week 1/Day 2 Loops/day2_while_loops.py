print()

# basic counting using while loop 
count = 1
n = int(input("Enter your number: "))
print(f"\nCounting from 1 to {n} : ")

while count <= n:
    print(count)

    count += 1

print()


# sum of odd numbers
i = 1
total = 0
num1 = int(input("Enter your number: "))
print(f"\nOdd numbers from 1 to {num1} : ")

while i <= num1:
    print(i)
    total += i
    i += 2

print(f"\nThe grand total of first {num1} odd numbers is: {total} ")

print()
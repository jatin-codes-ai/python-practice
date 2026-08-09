print()

# print even numbers
n = int(input("Enter your number: "))
print(f"\nEven numbers from 1 to {n}:")
for i in range(2,n+1,2):
    print(i)

# Multiplication table
num1 = int(input("\nEnter your number: "))
print(f"\n---- Table of {num1} ----")

for i in range(1,11):
    print(f"{num1} X {i:2} = {num1*i:2}")

# sum of first n numbers
total = 0 
n = int(input("\nEnter your number: "))

for i in range(1,n+1):
    print(i)
    total += i

print(f"\nThe grand total of first {n} numbers is: {total}")

print()


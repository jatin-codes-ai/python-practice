print()

# Multiplication table
num1 = int(input("Enter your number: "))
print(f"---- Table of {num1} ----")

for i in range(1,11):
    print(f"{num1} X {i} = {num1*i}")

# sum of first n numbers
total = 0 
n = int(input("Enter your number: "))

for i in range(1,n+1):
    total += i

print(f"The grand total of first {n} numbers is: {total}")

print()
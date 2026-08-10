# List foundation

print()
fruits = ["mango", "banana", "apple", "orange"]
numbers = [10, 25, 3, 67, 42, 18]
mixed = [1, "hello", True, 3.14]

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Second fruit:", fruits[1])

print("Total fruits:", len(fruits))

fruits.append("grape")
print("After adding grape:", fruits )

fruits.remove("banana")
print("After removing banana:", fruits)

print("\n All fruits:")
for fruit in fruits:
    print("-", fruit)

print("Biggest number :" , max(numbers))
print("Smallest number :", min(numbers))
print("Sum of all numbers :", sum(numbers))

print()
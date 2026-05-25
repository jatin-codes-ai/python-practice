# Even/odd checker

print()

# Title name
print("="*20 + 'Even/Odd Checker' + "="*20)

# Even/odd logic
def is_even(number) :
    return number % 2 == 0 
       

# list of numbers
count = int(input("How many numbers to check?: "))
num_list = []
even = []
odd = []

# looping on list 
i = 1
if count == 0 :
    print("No number given.")
    
while i <= count :

    print()
    ip = int(input(f"Enter number {i}: "))
    num_list.append(ip)

    # if count :
    
    # function call
    if is_even(ip) :
                print(f"{ip} is even.")
                even.append(ip)
    else: 
                print(f"{ip} is odd.")
                odd.append(ip)
    i += 1
    
print(f"\nTotal: {count} numbers")
if len(even) :
    print(f"Even numbers: {even}")
    print(f"Biggest even number: {max(even)}")
    print(f"Smallest even number: {min(even)}")
    print(f"Even: {len(even)}")

if len(odd) :
    print(f"\nOdd numbers: {odd}")
    print(f"Biggest odd number: {max(odd)}")
    print(f"Smallest odd number: {min(odd)}")
    print(f"Odd: {len(odd)}")


# Ending        
print('='*60)

print()
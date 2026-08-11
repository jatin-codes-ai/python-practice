# Even/odd checker

print()

# Title name
print("="*20 + 'Even/Odd Checker' + "="*20)

# Even/odd logic
def is_even(number) :
    return number % 2 == 0 
       
while True :
    # list of numbers
    count = int(input("How many numbers to check?: "))
    num_list = []
    even = []
    odd = []

    # looping on list 
    if count == 0 :
        print("No number given.")
    
    for i in range(1, count + 1) :

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
    
    print(f"\nNumbers entered: {num_list}")
    print(f"Total: {count} numbers")
    if len(even) :
        print(f"\nEven numbers: {even}")
        print(f"Biggest even number: {max(even)}")
        print(f"Smallest even number: {min(even)}")
        print(f"Even: {len(even)}")

    if len(odd) :
        print(f"\nOdd numbers: {odd}")
        print(f"Biggest odd number: {max(odd)}")
        print(f"Smallest odd number: {min(odd)}")
        print(f"Odd: {len(odd)}")

    while True :
        again = input("want to check more numbers(Y/N): ").upper()

        if not (again == 'Y' or again == 'N') :
            print("Try again.")

        else :
             break
        
    if again == 'N' :
         print("Thank you!")
         break
    print("Continuing...")
    

    
    
    


# Ending        
print('='*60)

print()
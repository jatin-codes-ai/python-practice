# Bank account 

print()

print('='*10 + "Simple Bank" + '='*10)

curr_balance = 1000

new_balance = curr_balance

def deposit(amount) :
    
    if amount > 0  :
        return f"${amount} deposited"
    return 'Insufficient deposit.'

def withdraw(amount) :
    
    if amount <= new_balance :
        return f"${amount} withdrawn."
    return 'Insufficient balance.'

def check_balance() :
    return f"Current balance: ${new_balance}"




while True : 

    print("\n1. Deposit\n2. Withdraw\n3. Check\n4. Exit")

    ip = int(input("\nEnter your option: "))

    if ip == 1 :
        amount = int(input("Amount to deposit: "))
        print(deposit(amount))
        new_balance = new_balance + amount
    elif ip == 2 :
        amount = int(input("Amount to withdraw: "))
        print(withdraw(amount))
        new_balance = new_balance - amount
    elif ip == 3 :
        print(check_balance())
    elif ip == 4 :
        print("\nExiting...\nHave a nice day.")
        break
    else: 
        print('Please choose an option from above.')

print('='*27)

print()


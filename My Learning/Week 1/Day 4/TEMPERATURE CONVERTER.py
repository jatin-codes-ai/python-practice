# TEMPERATURE CONVERTER

print()

# Title name
print("="*20 + 'TEMPERATURE CONVERTER' + "="*20)
print()


print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Exit")


def convert(ip) :

    if not (1 <= ip <= 4) :
        op = "Invalid option."
    elif ip == 1 :
        cel = int(input("Enter Temp in celsius: "))
        op = f"Temp in Fahrenheit: {(cel * 9/5) + 32}"
    elif ip == 2 :
        fah = int(input("Enter Temp in fahrenheit: "))
        op =  f"Temp in Celsius: {(fah-32) * 5/9}"
    elif ip == 3 :
        cel = int(input("Enter Temp in celsius: "))
        op = f"Temp in kelvin: {cel + 273.15}"
    else :
        op = 'Exiting...\nThank you!'

    return op
    

while True :
    ip = int(input("\nWhich option do you wanna use?: "))
    print(convert(ip))
    if ip == 4 :
        break


# Ending        
print('='*60)

print()

    



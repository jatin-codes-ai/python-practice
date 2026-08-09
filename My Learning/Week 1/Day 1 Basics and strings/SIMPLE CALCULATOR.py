# SIMPLE CALCULATOR
print()

# input1
num1 = float(input("Enter your 1st number: "))
output = None
# operator
op = input("Choose any one operation(+,-,*,/) : ")

# operator acceptance
if op == '+' or op == '-' or op == '*' or op == '/' :
    print("operation accepted.")

# input2
    num2 = float(input("Enter your 2nd number: "))

# processing
    if op == '+' :
        output = num1 + num2
    elif op == '-':
        output = num1 - num2
    elif op == '*' :
        output = num1 * num2
    else:
        if num2 == 0:
            print("Error: cannot divide by zero")
        else:
            output = num1 / num2


# output
    # initialise variable method
    if output is not None :
        print(f"Answer = {output}")

else:
   print("operation not accepted.")


print()

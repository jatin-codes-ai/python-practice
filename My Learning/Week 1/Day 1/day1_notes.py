print("")
# Multi-line print
print('''\nI'm in seclusion and I'm building myself. 
But when I breakthrough I will conquer this world.\n''' )

# Python text to speech
import pyttsx3
engine = pyttsx3.init()
print("Meow ghop ghop ghop\n")
engine.say ("I'm in seclusion and I'm building myself. But when I breakthrough I will conquer this world.")
engine.runAndWait()

# Type function and typecasting
a = 1.5
print(type(a))

a = "5.8"
b = float(a)
t = type(b)
print(t)

# input function and sum of 2 nos 
c = input("Give input : ")
print(type(c))

d = int(input("Enter no.1 :"))
e = int(input("Enter no.2 :"))
print(type(d))

print("Sum of d and e is :", d + e)

# strings 

name = "Jatin"
sl = name[0:5:2]
print(f"Slicing name with interval 2  : {sl}")
print(f"Length of name is : {len(name)}")
print(f"My name starts with Ja : {name.startswith("Ja")}")
print(f"My name ends with in : {name.endswith("in")}")
print(f"No. of times 't' occur in my name : {name.count("t")}")
print(f"Where is 'i' in my name? : {name.find("i")}")
print(f"My name if t changes with l and n changes with m : {name.replace("t", "l").replace("n","m")}")



print("")
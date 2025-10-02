print("sfsf") 
print("sfsf", "ch")
print(34 + 34)

name = "Sdfs"
age = 23
age2 = age
price = 24.99
print("My name is:",name)
print("My age is:",age2)
print("My Bank Balance is:",price)

"""
Rules for identifiers
1. Identifiers can be a combination of uppercase, lowercase letters, digits or an underscore(_)
2. An identifier cannot start with a digit.
3. We cannot use special symbols in identifiers.
4. Identifiers can be of any length.
"""

print(type(name))
print(type(age2))
print(type(price))

"""
Datatypes in Python
1. Integer ( +ve, -ve , 0)
2. String ("s", 's', '''e''')
3. Boolean (True, False)
4. Float (2.23,2534.34)
5. None 
"""

a = None 
b = False
print(type(a))
print(a)
print(type(b))
print(b)

# Keywords in python cannot be used as identifiers.
# Python is a case-sensitive language.

# Print Sum of two numbers
A = 12
B = 23
sum = A + B
print(sum)

# Type Conversion
# 1. Type Conversion (Automatic)
# 2. Type Casting (Manual)

a = "2"
c = int(a)
print(type(c))
b = 23.34
print(c + b)

age = int(input("Enter your age: ")) # Result is always a string
print("Your age is:", age)
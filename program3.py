# String is a data type that stores a sequence of characters.
# Escape Sequence characters are used for formating
str1 = "ksfksbf.\nwkfbwokf"
str2 = "sfsfs.\tsfssfsd"
print(str1)
print(str2)
# Basic Operations in a String
# 1. Concatenation
# 2. length of the string
str3 = "hello"
str4 = "world"
print(str3 + str4)
print(len(str4))

# Slicing: Acessing parts of a string
str5 = "hello world"
print(str5[0:11])#Ending index is not included, but starting one is
#Negative Slicing

print(str5[-10:-1])

#String Functions
print(str5.endswith("er"))
print(str5.capitalize())
print(str5.replace("o","a"))
print(str5.find("o"))
print(str5.count("o"))

#Example

name = str(input("Enter your name:"))
print(len(name))

Price = str(input("Enter the Price of the Object:"))
print(Price.count("$"))
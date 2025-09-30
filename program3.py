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

# name = str(input("Enter your name:"))
# print(len(name))

# Price = str(input("Enter the Price of the Object:"))
# print(Price.count("$"))
# elif is used only when the first statement is true.
# else is written only once.

#Check if the number is odd or even

num1 = int(input("Enter the number:"))
if(num1 % 2 == 0):
    print("The number is Even")
else:
    print("The number is Odd")

#Greatest of Three numbers

num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))
if(num1 >= num2 and num1 >= num3):
    print("The num1 is the greatest of all three elements")
elif(num2 >= num3):
    print("The num2 is the greatest of all three elements")
else:
    print("The num3 is thre greatest of all three elements")

# #Check if the number is a multiple of 7

# num4 = int(input("Enter the number: "))
# if(num4 % 7 == 0):
#     print("The number is a multiple of 7")
# else:
#     print("The number is not a multiple of 7")
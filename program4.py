marks = [123,23424,23243,22]
print(marks)
print(type(marks))
print(marks[0])
print(marks[2])
print(len(marks))

#List stores elements of different types (unlike arrays)
#It is a built in data type that stores different types of values.
# Strings are immutable while lists are mutable.

marks.append(1)
marks.reverse()
marks.insert(0,34)
marks.sort()
marks.sort(reverse=True)
marks.remove(123) # removes the first occurence of the element
marks.pop(3) # removes the element at idx 4
print(marks)

## Tuples
# It is a built in datatype that lets us create an immutable sequence of values

tup = (2,2,2,2334,345)
print(tup[0])
print(tup.index(2)) # removes the first occurence of the element 
print(tup.count(2))

movies = []
# mov1 = input("Enter the name of movie:")
# mov2 = input("Enter the name of movie:")
# mov3 = input("Enter the name of movie:")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

# list = [1,2,3,2,1]
# list2 = list[::-1]
# if(list == list2):
#     print("It is a pallindrome.")
# else:
#     print("It is not a pallindrome.")

tup = ["C","D","A","A","B","B"]
print(tup.count("A"))
tup.sort()
print(tup)
#Dictioneries
#They are used to store data values in key:value pairs.
# They are unordered, mutable and don't allow duplicate keys.
# String, list and tuple are ordered.They have indexes.
info = {
    "name" : "abc",
    "job" : "abc",
    "Role" : "TPM",
    "age" : 35,
    23 : 234
}
a = {}
print(a)
a["name"] = "eds"
print(a)
print(info)
print(info["name"])
print(info[23])

#Nested Dictioneries

students = {
    "name" : "Abc",
    "subjects" : {
        "math": 23,
        "sci" : 35
    }
}

print(students["subjects"]["math"])
print(students.keys())
print(list(students.values()))
print(students.items())
print(students.get("subjects"))

# Sets
# It is a collection of unordered items, each item in a set is unique and immutable.
collection = set()# This is a set
col = {} # This is a dict
# sets are mutable
# The elements inside a set are immutable
# Unhashable : sets, list, dicts 

Word_dict = {
    "Table" : ["A piece of furniture","list of facts and figures"],
    "Cat" : "A small animal"
}
print(Word_dict)
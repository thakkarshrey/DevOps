# Strings
str1 = "alpha"
str2 = 'alpha'
str3 = '''next string'''
str4 = """next string"""

# Numbers
num1 = 34
flt1 = 4.2

# Lists - It is mutable
first_list = [str1, "DevOps", 45, num1, 3.4]
print(first_list)

# Tuple - It is not mutable
first_tuple = (str1, "DevOps", 45, num1, 3.4)
print(first_tuple)

# Dictionary - It is described using key value pairs
first_dictionary = {
    "name" : "Shrey",
    "weight" : 77,
    "age" : 26,
    "exercises" : ["Gym", "Football"]
}
print(first_dictionary)

print(type(first_list))
print(type(first_tuple))
print(type(first_dictionary))

# Boolean
x = True
y = False

print(x, y, type(x), type(y))
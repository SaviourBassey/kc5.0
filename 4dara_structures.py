# int, float, str, bool 

# DATA STRUCTURE
# list, dict, tuple, set


# ways of organizing, storing, and managing data efficiently to perform opetions effectively


# name = "Kodecamp"

# age = 100



# LIST DATA STRUCTURE - DATA TYPE IN PYTHON

# LIST is basically an ordered mutable collection of items, seperated by commas and enclosed in a square bracket. 
# these items can be of any data type in python
# they support duplication

# len() 
# sum(), min(), max()



# TUPLE is basically an ordered immutable collection of items, seperated by commas and enclosed in a parenthese(). 
# these items can be of any data type in python
# they support duplication 



# DICTIONARY is basically an unordered  collection of key-value pair, seperated by commas and enclosed in a curly braces{}. 
# they keys are unique and immutatble, there are commonly strings. numbers, tuple
# the values can be of any data type in python and there are mutable



# mixed_type = [100, 17.5, True, "Kodecamp"]

# print(ages)
# print()
# print(mixed_type)


# # ACCESSING A LIST ITEM
# # syntax:
# # list_name[index]

# print(ages[-1])


# CHANGING OF LIST ITEMS
# syntax:
# list_name[index] = NEW VALUE


# item_count = len(ages)
# print(item_count)
# ages[item_count-1] = 100



# # LIST METHODS
# # list_name.method_name()

# # HEAP: ages, 
# # STACK: re

# NEW_AGES = ages.copy()
# NEW_AGES.append("hello")


# for item in ages:
#     final_mult = item * final_mult 
#     final_mult *= item


# print(final_mult)
    


gender = ("male", "female", "female", "female", "male")




# # ACCESSING A LIST ITEM
# # syntax:
# # tuple_name[index]

# print(gender[0])


# tuple METHODS
# count & index
# print(gender.index("female"))



ages = { "student1": 20, "stedent3": 60, "student2": 40 }


# ACCESSING OF ITEM
# # syntax:
# # DICT_name[key]

# print(ages["student10"])


print(ages.get("student10"))


# CHANGING DICT VALUE
# # syntax:
# # DICT_name[key] = NEW_VALUE

ages["student2"] = 100





# ADDING DICT VALUE
# # syntax:
# # DICT_name[key] = NEW_VALUE

ages["student4"] = 100

print(ages)



# # DICTIONARY METHODS
# # dict_name.method_name()
print(ages.items())








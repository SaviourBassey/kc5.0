# CONTROL FLOW: is basically the order of execution of our programs


# conditionals: is basic the ability for our program to make choices

# 3 KEYWORDS USED TO CONSTRUCT CONDITIONAL STATEMENT
# if, else, elif

# if: it only execute your specified code on when a condition is True 

# condition in programming refers to an expression (3+3-1, 10/2) that must evaluate to a boolean value (Ture/False)

# Conditional Operators: >, <, >=, <=, ==, !=

# logical Operators: we can used these operators in conjunction with the conditional operators to 
# construct a more complex condition: 

# and: both sides must be True for the result to be True
# or: atleast one side must be True for the result to be True
# not: negate the boolean value


# else: is used in conjunction with the if statement, to only execute your specified code when the 
# condition of the if statament is false

# elif: it is a short form for else if, used in conjunction with the if statement, to contruct statement for 
# other conditions




# SYNTAX:
# if condition:
#     your specified code to be executed
#     your specified code to be executed
#     your specified code to be executed
# elif condition:
#     specified code
#     specified code
#     specified code
#     specified code
#     specified code
# else:
#     specified code
#     specified code
#     specified code
#     specified code




# NESTING IN CONDITIONAL:  having conditional statement inside another condtional statement


# if condition:
#     if condition:
#         if condition:
#             specified code to be executed
#         elif condition:
#             specified code to be executed
#         elif condition:
#             specified code to be executed
#         else:
#             specified code to be executed
#     elif condition:
#         specified code to be executed
#     elif condition:
#         specified code to be executed
#     else:
#         specified code to be executed
# elif condition:
#     if condition:
#         specified code to be executed
#     elif condition:
#         specified code to be executed
#     elif condition:
#         specified code to be executed
#     else:
#         specified code to be executed
# elif condition:
#     if condition:
#         specified code to be executed
#     elif condition:
#         specified code to be executed
#     elif condition:
#         specified code to be executed
#     else:
#         specified code to be executed
# else:
#     if condition:
#         specified code to be executed
#     elif condition:
#         specified code to be executed
#     elif condition:
#         specified code to be executed
#     else:
#         specified code to be executed



age = int(input("Entre your age: "))
print("Chosse Gender Below")
print("1. Male                                                         2.Female")
gender = int(input("Choose: "))


if age == 18:
    if gender == 1:
        print("Hello Sir, I am an adult")
    elif gender == 2:
        print("Hello Ma, I am an adult")
    else:
        print("Invalid Gender Choice")
elif age == 90:
    print("You are old")
elif age == 70:
    print("You are matured")
else: 
    print("I am not an adult")






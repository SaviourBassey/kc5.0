# loop is basically repeatition

# 2 TYPES OF LOOPS: for loop & while loop


# for loop: that repeat a portion of our code based on a number of item in a structure
    

# while loop: that repeat a portion of our code based on a condition that True



# mango, apple, pineapple


# range(10-5) - 0,1,2,3,4


# FOR LOOP SYNTAX

# for variable_name | _ in structure:
#     portion of code to execute
#     portion of code to execute
#     portion of code to execute
#     portion of code to execute
#     portion of code to execute
#     portion of code to execute
#     portion of code to execute


# WHILE LOOP SYNTAX

# while condition:
#     portion of code to execute
#     portion of code to execute
#     portion of code to execute
#     portion of code to execute
#     portion of code to execute
#     portion of code to execute



# LOOP KEYWORDS:  the are basically keywords that ulter the default behaviour of a loop

# break: it terminet the loop before time 

# continue: it skips current iteration to a new one



# NESTED LOOPS: there are basically loops in loops


# 1 iteration of the outer loop, the inner iterate completely



# hour loop - minute loop - seconds loop




for _ in range(10):
    print("OUTTER LOOP")

    for _ in range(10):
        print("Inner loop")
        print()





grand_total = 0


# for item in range(5): # 0,1,2,3,4

#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))


#     result = num1 + num2

#     grand_total = grand_total + result

#     # rusesult + result + result + result + result=


#     print("The addition of ", num1, "and", num2, "is",result)

#     print()




# print("The end")
# print(grand_total)

a = int(input("Enter number for a: "))
b = int(input("Enter number for b: "))



while a>b:

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 + num2

    print("The addition of ", num1, "and", num2, "is",result)

    print()
    
    if num2 > 100:
        break



print("The end")
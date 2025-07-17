# # print()
# # print()


# # FUNCTION is basically a collection of USEABLE code that perform a specific action 


# # grouping source code, we them reuse that source code without re-writing the source code



# # whenusing functions: 2 steps are involved

# # - create / initialiaze the function
# # - calling / invoking the function



# # def functiona_name (optional parameters):
# #     body body
# #     body body
# #     body body
# #     body body
# #     body body
# #     optional retun statement



# # FUNCTION INCATION:

# # functiona_name(optinal argument)


# # DIFF B/W FUNC PARAMETERS & FUNC ARGUMENT:

# # parameters are moe like placeholders for the actual values
    
# # argument is the actual 

# # variable scoping: 



# # NB: by default FUNCTION BODY IS LOCAL TO THE FUNCTION, everything that happens within that function will stay 
# # within that function

# # but if there is need to send out information from a function, we use the retunrn statemet in the this manner: 

# # retun value_to_be_sent_out

# # in this case, only value_to_be_sent_out, can leave the function




# num1 = 50
# num2 = 30


# def multplication (num1, num2):
#     result = num1*num2
#     return result, "another value", 30




# def age_mult (age,multiplier):
#     mult = age * multiplier
#     print(mult)



# def first_function(name, age):
#     print("hello", name)
#     print("you are", age, "years old")



# a,b,c = multplication(10,10) #decoupling



# print(a)
# print(b)
# print(c)

# # a = multplication(10,10)
# # print(a)


# # final_result =  a + 100

# # print(final_result)




# # first_function(100, "saviour")

# # print("Hello Kodecampers")

# # print("How are you?")


# # first_function()
# # # num1 = int(input("Enter a number: "))
# # # num2 = int(input("Enter a number: "))
# # # result = num1+num2
# # # print(result)


# # print("Hi")

# # # num1 = int(input("Enter a number: "))
# # # num2 = int(input("Enter a number: "))
# # # result = num1+num2
# # # print(result)

# # first_function()


# EXCEPTIONS: they are errors that occur during prohram execution


# ZeroDivisionError
# ValueError
# NameError

# try / except


# try:
#     # code that might cause problem during execution
# except optional ExceptionType:
#     # code to excute when there is problem


# try - takes in portion of code that you as the developer feel it might cause problem during execution

# except - take the portion of code that should execute if there is problem

# finally / else

a = 10

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = num1 / num2
    print(a)
except ValueError:
    print("problem with user input")
    result  = 0
except ZeroDivisionError:
    print("problem with division")
    result  = 0
except:
    print("problem with the code")
    result = 0






print(result)


print("Other codes")
print("Another codes")
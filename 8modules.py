# what is exactly is modules:
# python files that contains your variables, functions, and classes. They are basically your python scripts

# they can be included in another python script


# 3 TYPES OF MODULES:
# custom modules 
# built-in modules 
# thrid-party 


# 2 kinds of importation:

# entire modules importation

# specific importation


# entire importation:

# import module_name


# specific importation:

# from module_name import specific_func/var/classes


# statistics, json, os, datetime, , math







# a python scripts for children game: addition, subtraction, multiplication, add scores


# 1 score that would track for each game
# 2. we need show the menu (addition, subtraction, multiplication )
# 3. if user choice is 1 and make sure is number:
#     give two random number
#     ask user for the reult
#     also make sure that result is number
#     if correct, then i would increase score
#     if wrong, i would do nothing


# dict - object
# list, tuple - array
# str - string
# int,float - number, 
# bool - boolean 
# none - null



import mod
import random
import json

import mod
from mod import menu




score = {
    "addition": 0,
    "subtraction": 0,
    "multiplication": 0
}


dict_form = None
try: 
    with open("score.json", "r") as file:
        dict_form = json.load(file)
        dict_form = dict_form
except:
    with open("score.json", "w") as file:
        dict_form = json.dump(score, file)
        dict_form = dict_form

 
    


while True:
    mod.menu()


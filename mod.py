from mod2 import addition as add
import json




def menu():
    user_addition = 0


    print("--------------------------------------------------------------")
    print("-                                                            -")
    print("-           WELCOME TO KODECAMP CHILDREN'S GAME              -")
    print("-                                                            -")
    print("-                                                            -")
    print("-            Choose the option below                         -")
    print("-                                                            -")
    print("-                 1. Addition                                -")
    print("-                 2. Subtraction                             -")
    print("-                 3. Multiplication                          -")
    print("-                                                            -")
    print("--------------------------------------------------------------")
    print()

    while True:
        try:
            option = int(input("Enter: "))
            break
        except ValueError:
            print("Enter a valdid Number")
            print()
            continue

    if option == 1:
        for item in range(2):
            print()
            num1, num2 = add()
            print(f"What is the addition of: {num1} + {num2}")
            while True:
                try:
                    answer = int(input("Enter: "))
                    break
                except ValueError:
                    print("Enter a valdid Number")
                    print()
                    continue

            if answer == (num2 + num1):
                user_addition = user_addition + 1
            else:
                print("You are wrong")

            if item == 1:
                print()
                print(f"Your total score for the sddition game is: {user_addition}")
                print()
                print()

                dict_form = None
                try: 
                    with open("score.json", "r") as file:
                        dict_form = json.load(file)
                        dict_form = dict_form
                except:
                    print("Unable to save score at the moment")
                else:
                    dict_form["addition"] = user_addition

                    with open("score.json", "w") as file:
                        dict_form = json.dump(dict_form, file)



                


    
    









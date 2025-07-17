'''
Task 3: Calculator with History

Scenario: A basic calculator that remembers past results.

Instructions:

- Show options: Add, Subtract, Multiply, Divide, View History, Exit

- Use input to take two numbers and perform operation

- Store each operation and result in a list

- Show history with index numbers

- Use functions for operations and error handling for divide-by-zero
'''


# add, sub, div, mult


history = []

def adding():
    number_count = int(input("How many numbers do you want to add: "))
    number_list = []
    hist_statement = ""
    for i in range(number_count):
        try:
            num = int(input("Enter number: "))
            number_list.append(num)
        except:
            print("Number must be valid integers")
            print()
            continue

    result = sum(number_list)
    print(result)

    for num in number_list:
        if number_list.index(num) == len(number_list)-1:
            hist_statement = hist_statement + str(num) + " = "
        else:
            hist_statement = hist_statement + str(num) + " + "

    
    hist_statement = hist_statement + str(result)
    print(hist_statement)
        
    history.append(hist_statement)



def menu():
    print("--------------------------------------------------------------")
    print("-                                                            -")
    print("-           WELCOME TO OUR CALCULATOR                        -")
    print("-                                                            -")
    print("-                                                            -")
    print("-            Choose the option below                         -")
    print("-                                                            -")
    print("-                 1. Add                                     -")
    print("-                 2. Divide                                  -")
    print("-                 3. View History                            -")
    print("-                                                            -")
    print("--------------------------------------------------------------")
    print()

    while True:
        try:
            option = int(input("Enter: "))

            if option not in [1,2,3]:
                print("Enter a valdid Option")
                print()
                continue

            break
        except ValueError:
            print("Enter a valdid Number")
            print()
            continue

    if option == 1:
        while True:
            adding()
            print()
            print("1. Add another number")
            print("2. Main Menu")
            while True:
                try:
                    opt = int(input("Enter: "))

                    if opt not in [1,2]:
                        print("Enter a valdid Option")
                        print()
                        continue

                    break
                except ValueError:
                    print("Enter a valdid Number")
                    print()
                    continue


menu()
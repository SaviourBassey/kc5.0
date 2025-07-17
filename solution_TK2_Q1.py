'''
Task 1: Student Management System

Goal: Build a program to store student names and their scores using lists/dictionaries.

Core Features:

- Add new students (with 3 subject scores)

- Show all students with average and performance status

- Search for a student by name

- Use functions for actions

- Use error handling for invalid inputs

 
'''
# data structure: list, dict, tuple, set
# function

# D = {
#     "name": {"email": email1, "name": name1},
#     "name2": { "email": email2,"name": name2}
# }

# for item in D: 
#     for item in D[name]:
#         D[name][email]
#         name
#     d[name2]


# what management system is and where is will be applied?
# student = add, edit, get, delete

# CRUD - CREATE, READ, UPDATE, DELETE

# what student dretails do i need to add system?

# add:
# student credentials (name, score 1, score 2, score 3)

# get: all student with their average and status (pass (above 50) / failed)


# get: with the student name


std_db = {}



def add_student():
    student_name = input("Enter a student name: ")
    while True:
        try: 
            score1 = int(input("Enter a score for subject 1: "))
            score2 = int(input("Enter a score for subject 2: "))
            score3 = int(input("Enter a score for subject 3: "))
            break
        except:
            continue

    average = (score1 + score2 + score3) / 3
    status = None

    if average >= 50:
        status = "passed"
    else:
        status = "failed"

    std_db[student_name] = {
        "score1": score1,
        "score2": score2,
        "score3": score3,
        "average": average,
        "status": status
    }



def view_all_students():
    for element in std_db:
        print(f"STUDENT NAME: {element}")
        for item in std_db[element]:
            if item == "score1":
                print(f"STUDENT SCORE 1: {std_db[element][item]}")
            elif item == "score2":
                print(f"STUDENT SCORE 2: {std_db[element][item]}")
            elif item == "score3":
                print(f"STUDENT SCORE 3: {std_db[element][item]}")
            elif item == "average":
                print(f"STUDENT AVERAGE: {std_db[element][item]}")
            elif item == "status":
                print(f"STUDENT STATUS: {std_db[element][item]}")

        print()



def search_students():
    while True:
        student_name = input("Enter Student Name: ")

        try:
            for element in std_db[student_name]:
                if element == "score1":
                    print(f"STUDENT SCORE 1: {std_db[student_name][element]}")
                elif element == "score2":
                    print(f"STUDENT SCORE 2: {std_db[student_name][element]}")
                elif element == "score3":
                    print(f"STUDENT SCORE 3: {std_db[student_name][element]}")
                elif element == "average":
                    print(f"STUDENT AVERAGE: {std_db[student_name][element]}")
                elif element == "status":
                    print(f"STUDENT STATUS: {std_db[student_name][element]}")


            print()
            print("1. Search another stdudent")
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

            if opt == 1:
                print()
                continue
            else:
                menu()
                break

        except KeyError:
            print()
            print("Student not found")
            print()
            continue

        


def menu():
    print("--------------------------------------------------------------")
    print("-                                                            -")
    print("-           WELCOME TO STUDENT MGT SYSTEM                    -")
    print("-                                                            -")
    print("-                                                            -")
    print("-            Choose the option below                         -")
    print("-                                                            -")
    print("-                 1. Add Student                             -")
    print("-                 2. View all Student                        -")
    print("-                 3. Search a Student                        -")
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
            add_student()
            print()
            print("1. Add another stdudent")
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

            if opt == 1:
                print()
                continue
            else:
                break
        
        print()
        menu()


    elif option == 2:
        print()
        view_all_students()
        print()
        menu()


    elif option == 3:
        print()
        search_students()



menu()










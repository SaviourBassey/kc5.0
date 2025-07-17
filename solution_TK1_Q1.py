'''
Task 1: Student Grade Evaluator

Scenario: Collect and evaluate grades for multiple students

Instructions:

- Ask how many students to process.
- Use a loop to:

     - Ask for each student's name and 3 subject scores.

     - Convert scores to float, calculate the average.

     - Display result:

     - Average < 50 -> Fail

     - 50-79 -> Pass

     - 80+ -> Excellent!
- After all students are processed, display a summary: how many passed, failed, and got excellent
'''

# loops & condition

# AREA OF A TRIANGLE = 1/2 X b X h

# UNDERSTAND THE TASK (what) - ALGORITHM - (how) - CODING


# collect value for height - input()
# collect value for breadth - input()
# carry out the calculation - arith ops to carry out the cal
# show the result of the calculation the enduser -print()

# repeat all over again - everythin and insert in a loop



number_of_student = int(input("How amny student is to be processed: ")) 


# tracker
passed = 0
failed = 0
excellent = 0


for i in range(number_of_student):
    student_name = input("Enter a student name: ")
    score1 = int(input("Enter a score for subject 1: "))
    score2 = int(input("Enter a score for subject 2: "))
    score3 = int(input("Enter a score for subject 3: "))

    average = float((score1 + score2 + score3)) / 3

    if average >= 80:
        excellent = excellent + 1
        print("You have Excellent")
    elif average >= 50 and average <= 79:
        passed = passed + 1
        print("You have Passed")
    else:
        failed = failed + 1
        print("You have Failed")

    print()
    print("moving onto the next student ....")
    print()



print("EVALUATION SUMMARY")
print("The total number of student that have excellent: ", excellent)
print("The total number of student that have passed: ", passed)
print("The total number of student that have failed: ", failed)
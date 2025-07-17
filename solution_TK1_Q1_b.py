number_of_student = int(input("How amny student is to be processed: ")) 
number_of_course = int(input("How amny Courses is to be processed: ")) 


# tracker
passed = 0
failed = 0
excellent = 0

scores = 0


for i in range(number_of_student):
    student_name = input("Enter a student name: ")

    for j in range(number_of_course):
        subject_name = input("Enter the subject name: ")
        new_score = int(input(f"Enter a score for {subject_name}: "))
        scores = scores + new_score


    average = float(scores) / number_of_course

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
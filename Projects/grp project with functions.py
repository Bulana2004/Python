def inputs():
    students = []
    index = 1

    while True:
        choice = input(
            "\n1. Input student details\n2. Find student details using index number\n3. Exit the program\nEnter number to continue: ")

        # Student details add to list
        if choice == "1":
            # Inputs
            print("\nYour index number is:", index)
            name = input("Enter your name here: ")
            th_marks = int(input("Enter your theory marks: "))
            pr_marks = int(input("Enter your practical marks: "))
            pro_marks = int(input("Enter your project marks here: "))

            # Students list
            student_details = {"index number": index, "name": name,
                               "th marks": th_marks, "pr marks": pr_marks, "pro marks": pro_marks}
            students.append(student_details)

            # Calculate total marks and grade
            calculation(student_details)

            index += 1

        # Get student details
        elif choice == "2":
            for student_details in students:
                print(f"\nIndex: {
                      student_details['index number']} / Name: {student_details['name']}")

            enter_index = int(input("\nEnter your index number: "))
            found_student = None

            for student in students:
                if student["index number"] == enter_index:
                    found_student = student
                    break

            if found_student:
                print("\nFound student!")
                print("Name:", found_student["name"])
                calculation(found_student)
            else:
                print("Student not found!")

        # Exit the program
        elif choice == "3":
            break

        else:
            print("Invalid choice! Please enter a valid number.")

    print("\nThank you! End of program!")


def calculation(student_details):
    # Print total
    total = student_details["pr marks"] + \
        student_details["pro marks"] + student_details["th marks"]
    print("\nYour total marks are:", total)

    # Get grade
    average = total / 3

    if average <= 35:
        grade = "F"
    elif average < 50:
        grade = "S"
    elif average < 65:
        grade = "C"
    elif average < 75:
        grade = "B"
    elif average <= 100:
        grade = "A"
    else:
        print("Invalid!")
        return

    print("You got", grade, "pass!")

    # Get average
    print("Average marks are:", average)


inputs()

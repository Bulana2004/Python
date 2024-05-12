students = []
index = 1
while True:
    choice = input(
        "\n1.Input students details\n2.Find student details using index number\n3.Exit the programm\nEnter number to conrinue: ")

    # Student details add to list
    if choice == "1":
        # Inputs
        print("\nyour index number is: ", index)
        name = input("Enter your name hear: ")
        th_marks = int(input("Enter your theary marks: "))
        pr_marks = int(input("Enter your practicle marks: "))
        pro_marks = int(input("Enter you project marks hear: "))

        # Students list
        student_details = {"index number": index, "name": name,
                           "th marks": th_marks, "pr marks": pr_marks, "pro marks": pro_marks}
        students.append(student_details)

        # print total
        total = student_details["pr marks"] + \
            student_details["pro marks"]+student_details["th marks"]
        print("\nYour total marks are: ", total)

        # get grade
        avarage = total / 3

        if avarage <= 35:
            grade = "F"
        elif avarage < 50:
            grade = "S"
        elif avarage < 65:
            grade = "C"
        elif avarage < 75:
            grade = "B"
        elif avarage <= 100:
            grade = "A"
        else:
            print("Invalid!")
            continue

        print("You got ", grade, " pass!")

        # get avarage
        print("Avarage marks is: ", avarage)

        index += 1

    # Get student details
    elif choice == "2":
        for student_details in students:
            print(f"\nIndex: {student_details['index number']} /Name is: {
                  student_details["name"]}")

        enter_index = int(input("\nEnter your index number: "))
        found_student = None

        for student in students:
            if student["index number"] == enter_index:
                found_student = student
                break

        if found_student:
            print("\nFound student!")
            print("\nname: ", found_student["name"])
            total_marks = found_student["th marks"] + \
                found_student["pr marks"]+found_student["pro marks"]
            print("Total marks: ", total_marks)
            avarage_marks = total_marks / 3
            print("Avarage marks: ", avarage_marks)
            if avarage_marks <= 35:
                grade = "F"
            elif avarage_marks < 50:
                grade = "S"
            elif avarage_marks < 65:
                grade = "C"
            elif avarage_marks < 75:
                grade = "B"
            elif avarage_marks <= 100:
                grade = "A"
            else:
                print("Invalid!")
                continue

            print(" got ", grade, " pass!")

    # Exit the programm
    if choice == "3":
        break

print("\nThank you! End of programe!")

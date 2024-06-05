# append File function
def append_details_to_file():
    students = []
    max_index = 0
    with open("grp.txt") as read:
        lines = read.readlines()
        if lines:
            for line in lines:
                record = line.strip().split("|")
                if record and record[0].isdigit():
                    max_index = max(max_index, int(record[0]))
                max_index += 1
        else:
            max_index = 1

    read.close()

    with open("grp.txt", "a") as file:

        # User Inputs
        print(f"\nYour index is {max_index}")
        name = input("Enter your name: ")
        pr_marks = int(input("Enter your Practicle marks: "))
        th_marks = int(input("Enter your Theary marks: "))
        pro_marks = int(input("Enter your project marks: "))

        # Total marks
        total_marks = pr_marks + th_marks + pro_marks
        print(f"\nYour total marks are {total_marks}")
        # Avarage marks
        avarage_marks = total_marks / 3
        print(f"Your avarage marks are {avarage_marks}")
        # Grade
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
            return
        print(f"You got {grade}!")

        # Write content in file
        file.write(f"\n{str(max_index)}|{name}|{str(pr_marks)}|{
                   str(th_marks)}|{str(pro_marks)}|{str(total_marks)}|{str(avarage_marks)}|{str(grade)}")

        print("\nSuccesful Inputs!")

    file.close()


# Read file fuction
def read_details_in_file():
    students = []

    with open("grp.txt") as file:
        lines = file.readlines()
        # Remove the first line in .txt File
        marks_line = lines[1:]

        for line in marks_line:
            record = line.split("|")

            index = record[0].strip()
            name = record[1].strip()
            pr_marks = record[2].strip()
            th_marks = record[3].strip()
            pro_marks = record[4].strip()
            total_marks = record[5].strip()
            avarage_marks = record[6].strip()
            grade = record[7].strip()

            student_details = {
                "Index": index,
                "Name": name,
                "pr_marks": pr_marks,
                "th_marks": th_marks,
                "pro_marks": pro_marks,
                "Total": total_marks,
                "Avarage": avarage_marks,
                "Grade": grade
            }

            students.append(student_details)

    for student in students:
        print(f"\nStudent index: {student['Index']
                                  } || Name is: {student['Name']}")

    entered_index = int(input("\nEnter your desired index number: "))
    found_student = None
    entered_index = str(entered_index)

    for student in students:
        if student['Index'] == entered_index:
            found_student = student
            break

    if found_student:
        print("\nFind a details")
        print(f"Student name: {found_student['Name']}")
        print(f"Total marks are {found_student['Total']}\nAvarage marks are {
              found_student['Avarage']}\nGrade is {found_student['Grade']}!")
    else:
        print("\nEntered index number is not valid")

    file.close()


# Update file data function
def find_index_and_update_data():
    with open("grp.txt") as file:
        lines = file.readlines()

    for line in lines[1:]:
        record = line.split("|")
        index = record[0].strip()
        name = record[1].strip()
        print(f"\nIndex: {index} || Name: {name}")

    enter_index = input("\nEnter your desired index number to edit details: ")
    found_index = None

    for i, line in enumerate(lines[1:], start=1):  # Skip the header
        record = line.split("|")
        index = record[0].strip()
        if index == enter_index:
            found_index = i
            break

    if found_index is not None:
        record = lines[found_index].split("|")
        print(f"\nCurrent Student Details.\nName - {record[1].strip()}")
        print(f"Practical marks - {record[2].strip()}")
        print(f"Theory marks - {record[3].strip()}")
        print(f"Project marks - {record[4].strip()}")

        new_name = input("\nEnter Your Updated Name: ") or record[1].strip()
        new_pr_marks = input(
            "Enter New Practical marks: ") or record[2].strip()
        new_th_marks = input(
            "Enter your new Theory marks: ") or record[3].strip()
        new_pro_marks = input(
            "Enter your new Project marks: ") or record[4].strip()

        # Convert marks to integers for calculation
        new_pr_marks = int(new_pr_marks)
        new_th_marks = int(new_th_marks)
        new_pro_marks = int(new_pro_marks)

        # Calculate new total marks and average marks
        new_total_marks = new_pr_marks + new_th_marks + new_pro_marks
        new_avarage_marks = new_total_marks / 3

        # Determine new grade
        if new_avarage_marks <= 35:
            new_grade = "F"
        elif new_avarage_marks < 50:
            new_grade = "S"
        elif new_avarage_marks < 65:
            new_grade = "C"
        elif new_avarage_marks < 75:
            new_grade = "B"
        elif new_avarage_marks <= 100:
            new_grade = "A"
        else:
            print("Invalid!")

        # Update the record
        lines[found_index] = f"{record[0].strip()}|{new_name}|{new_pr_marks}|{new_th_marks}|{
            new_pro_marks}|{new_total_marks}|{new_avarage_marks}|{new_grade}\n"
    else:
        print("Student with the entered index number was not found.")

    # Write the updated data back to the file
    with open("grp.txt", "w") as file:
        file.writelines(lines)
    
    file.close()


# Programm Run
print("\nWelcome!")
while True:
    user_input = int(input(
        "\nRead the menu and start\n1.Enter Student Details (Enter 1)\n2.Find Student Details (Enter 2)\n3.Edit Input Details (Enter 3)\n4.Exit (Enter 4)\nEnter your menu numner: "))

    if user_input == 1:
        append_details_to_file()

    if user_input == 2:
        read_details_in_file()

    if user_input == 3:
        find_index_and_update_data()

    if user_input == 4:
        break

print("\nThank you!")

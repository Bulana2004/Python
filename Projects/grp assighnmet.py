students = []
while True:
    index = int(input("\nEnter your index number: "))
    name = input("Enter your name: ")
    th_marks = int(input("Enter your theary marks: "))
    pr_marks = int(input("Enter your practicle marks: "))
    pro_marks = int(input("Enter your project marks: "))

    student_details = {"index numb": index, "name": name,
                       "th_marks": th_marks, "pr_marks": pr_marks, "pro_marks": pro_marks}

    students.append(student_details)

    # Print the details of all entered students
    print("\nDetails of entered students:")
    for student in students:
        print("\nIndex Number:", student["index numb"])
        print("name:", student["name"])

        # Total marks
        total = student["th_marks"] + \
            student["pr_marks"] + student["pro_marks"]
        print("Total Marks = ", total)

        # Get grade
        x = total / 3
        if x <= 35:
            grade = "Fail!"
        elif 50 <= x < 65:
            grade = "Pass - C"
        elif x < 75:
            grade = "Pass - B"
        elif x <= 100:
            grade = "Pass - A"
        else:
            grade = "Invalid Marks"

        print(grade)

        # Get Avarage
        avarage = total / 3
        print("Avarage is = ", avarage)

        print(student_details)

    # asking user choice
    user_choice = input("\nWould You like to add another data (y,n) = ")
    x = user_choice[0].capitalize()
    if x != "Y":
        break

print("\t\nThank you!!")

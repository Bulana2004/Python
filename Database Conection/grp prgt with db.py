import mysql.connector
# db_connection = mysql.connector.connect(
#     host="localhost",
#     user="pythonDatabase",
#     passwd="1234",
#     database="mydata"
# )
# dbcursor = db_connection.cursor()
# dbcursor.execute("CREATE DATABASE mydata")
# dbcursor.execute("""
#     CREATE TABLE student_details (
#     )""")


def input_student_details():
    # Connect to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="pythonDatabase",
        passwd="1234",
        database="mydata"
    )
    mycursor = mydb.cursor()

    # Get the maximum ID from the student_details table
    mycursor.execute("SELECT MAX(id) FROM student_details")
    max_id_result = mycursor.fetchone()
    if max_id_result[0] is None:
        max_id = 0
    else:
        max_id = max_id_result[0]

    # the max_id for the new record
    new_id = max_id + 1

    # user for input
    print(f"\nYour id is {new_id}")
    name = input("Enter your name: ")
    pr_marks = int(input("Enter your practical marks: "))
    th_marks = int(input("Enter your theory marks: "))
    pro_marks = int(input("Enter your project marks: "))

    # Calculate total and average
    total = pr_marks + th_marks + pro_marks
    print(f"Your Total marks are {total}")
    average = total / 3
    print(f"Your Avarage marks are {average}")

    # Determine grade
    if average >= 90:
        grade = 'A'
    elif average >= 75:
        grade = 'B'
    elif average >= 50:
        grade = 'C'
    else:
        grade = 'F'

    print(f"You got {grade} pass!")

    # Insert data into the table
    sql = "INSERT INTO student_details (id, name, pr_marks, th_marks, pro_marks, total, average, grade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (new_id, name, pr_marks, th_marks, pro_marks, total, average, grade)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Data inserted successfully!")


def output_student_details():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="pythonDatabase",
            passwd="1234",
            database="mydata"
        )
        dbcursor = mydb.cursor()

        # Fetch student details from the database
        dbcursor.execute("SELECT * FROM student_details")
        records = dbcursor.fetchall()

        students = []
        for record in records:
            student_details = {
                "Index": record[0],
                "Name": record[1],
                "pr_marks": record[2],
                "th_marks": record[3],
                "pro_marks": record[4],
                "Total": record[5],
                "Average": record[6],
                "Grade": record[7]
            }
            students.append(student_details)

        # Print student details
        for student in students:
            print(f"\nStudent index: {
                  student['Index']} || Name: {student['Name']}")

        # Ask user for index number to find specific student details
        entered_index = input("\nEnter your desired index number: ").strip()

        try:
            # Convert entered index to integer
            entered_index = int(entered_index)
        except ValueError:
            print("\nEntered index number is not valid")
            return

        found_student = None

        for student in students:
            if student['Index'] == entered_index:
                found_student = student
                break

        if found_student:
            print("\nFound details:")
            print(f"Student name: {found_student['Name']}")
            print(f"Total marks: {found_student['Total']}")
            print(f"Average marks: {found_student['Average']}")
            print(f"Grade: {found_student['Grade']}")
            print(f"Practical Marks: {found_student['pr_marks']}")
            print(f"Theory Marks: {found_student['th_marks']}")
            print(f"Project Marks: {found_student['pro_marks']}")
        else:
            print("\nEntered index number is not valid")
    except mysql.connector.Error as err:
        print(f"Error: {err}")


# Programm Run
print("\nWelcome!")
while True:
    user_input = int(input(
        "\nRead the menu and start\n1.Enter Student Details (Enter 1)\n2.Find Student Details (Enter 2)\n3.Edit Input Details (Enter 3)\n4.Exit (Enter 4)\nEnter your menu numner: "))

    if user_input == 1:
        input_student_details()

    if user_input == 2:
        output_student_details()

    if user_input == 3:
        print()

    if user_input == 4:
        break

print("\nThank you!")

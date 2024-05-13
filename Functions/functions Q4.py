def marks():
    total_marks = 0
    for i in range(1, 11):
        input_marks = int(input("Enter your marks: "))
        total_marks += input_marks

    print("\nTotal marks: ",total_marks)
    avarage_marks = total_marks / 10

    if avarage_marks >= 50:
        print("Good!")
    else:
        print("Bad!")


marks()

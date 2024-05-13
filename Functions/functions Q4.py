def marks():
    avarage = input_marks / 10

    if avarage >= 50:
        print("Good!")
    else:
        print("Bad!")


for i in range(1, 11):
    input_marks = int(input("Enter the input_marks: "))

input_marks += input_marks

total = input_marks
print("\nTotal is: ", total)

marks()

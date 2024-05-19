while True:
    input_number = int(input("\nEnter your number here: "))

    if input_number >= 1:
        for i in range(2, input_number):
            if input_number % i == 0:
                print("\n(", input_number, ")", " Is not a primary key!")
                break
        else:
            print("\n(", input_number, ")", " Is a primary key!")
    else:
        print("\n(", input_number, ")", " Is not a primary key!")
    # Get user inputs
    choice = input("\nCheck another primary key (yes/no) : ")
    x = choice[0].lower()
    if x != "y":
        break
print("\nThank you!")

print("Welcome!!!")
while True:

    user_input = input("\n1.Number\n2.String\nYour choice: ")

    if user_input == "1":
        number = int(input("Enter your number: "))
        # int to str
        number_str = str(number)

        if number_str == number_str[::-1]:
            print(number, " This is a Palindoma number!")
        else:
            print(number, " This is not a Palindroma number!")

    elif user_input == "2":
        string = input("Enter your string hear:")

        if string == string[::-1]:
            print(string, " This is a Palindoma string!")
        else:
            print(string, " This is not a Palindroma srting!")

    else:
        print("Invalid input!")

    choice = input("\nCheck another one (yes/no): ")
    x = choice[0].lower()
    if x != "y":
        break
print("Thank you!")

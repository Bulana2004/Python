print("Welcome!!!")
while True:
    string = input("Enter your string hear:")

    if string == string[::-1]:
        print(string, " This is a Palindoma string!")
    else:
        print(string, " This is not a Palindroma srting!")

    choice = input("\nCheck another one (yes/no): ")
    x = choice[0].lower()
    if x != "y":
        break
print("Thank you!")

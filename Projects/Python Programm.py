print("Welcome our Calculator Project")

while True:
    # inputs
    numb1 = int(input("\nEnter your first Number = "))
    numb2 = int(input("Enter your second Number = "))
    oparator = input("Enter your oparator (+,-,*,/) = ")

    # Oparators
    if oparator == "+":
        print("\nYour answer is =", numb1+numb2)
    elif oparator == "-":
        print("\nYour answer is = ", numb1-numb2)
    elif oparator == "*":
        print("\nYour answer is = ", numb1*numb2)
    elif oparator == "/":
        if numb1 != 0:  # Check the devision by zero
            print("\nYour answer is = ", numb1/numb2)
        else:
            print("\nError: Can't divided by zero")
    else:
        print("\nEnter valid oparator")

    # Asking the user choice
    user_choice = input("\nWould You like to do another calculation (y,n) = ")
    x = user_choice[0].capitalize()
    if x == "N":
        break

print("\nThank you! \nPresent By GROUP-1")

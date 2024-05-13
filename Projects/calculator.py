def cal():

    while True:
        numb1 = float(input("\nEnter your number1: "))
        numb2 = float(input("Enter yuor number2: "))
        oparators = input("\nEnter your oparator (+,-,*,/):")

        if oparators == "+":
            answer = numb1 + numb2
        elif oparators == "-":
            answer = numb1 - numb2
        elif oparators == "*":
            answer = numb1 * numb2
        elif oparators == "/":
            if numb2 == 0:
                print("\nCan't devided by zero!")
                continue
            else:
                answer = numb1 / numb2
        else:
            print("\nInvalid input!")
            continue

        print("\nThe answer is: ", answer)

        choice = input(
            "\nWould you like to do another calculation (yes or no): ")
        x = choice[0].lower()
        if x != "y":
            break

    print("\nThank you!")

print("\nWelcome to small calculator!")
cal()

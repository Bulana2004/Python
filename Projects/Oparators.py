while True:
    print("Welcome to Oparators code genarator")

    # Number input
    numb1 = int(input("Enter Your numb1 = "))
    numb2 = int(input("Enter your numb2 = "))

    # oparators
    print("Additon")
    answer = numb1 + numb2
    print("Your Answer is = ", answer)

    print("\nSubstraction")
    answer = numb1 - numb2
    print("Your answer is = ", answer)

    print("\nMultiplying")
    answer = numb1 * numb2
    print("Your Answer is = ", answer)

    print("\nDeviding")
    if numb2 == 0:
        print("You can't divided by 0")
    else:
        answer = numb1 / numb2
        print("Your answer is = ", answer)

    # Asking the user choice
    user_choice = input("Doyo want to perform another calculation (y/n)")
    x = user_choice[0].capitalize
    if x.lower() != 'Y':
        break

print("Thank you continue with us :)")

def start_game():
    print("\tWelcome to the game of searching for thresher")
    user_choice = input(
        "\nOne day you are walking in a forest and you come across a cave. Are you into it or not? (yes or no): ").lower()

    if user_choice != "yes" and user_choice != "y":
        print("\nYou decide to return home. Thank you for playing!")
    else:
        print("You start the thresher hunting game!")
        cave()


def cave():
    print("You enter a cave it had a two ways to go!")
    user_choice = input("Enter where are you going (left/right)").lower()

    if user_choice == "l":
        print("you are meet the dragon")
    elif user_choice == "r":
        print("You are going right way")
        collecting()
    else:
        print("invalid input plz reenter the right way")
        cave()


def collecting():
    print("You are enter the tresher room")
    print("\nCongratulation you got the tresser")


start_game()

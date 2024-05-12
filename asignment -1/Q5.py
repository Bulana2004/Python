balance = 0
print("Welcome to reload machine programm!")
user_password = input("\nSet a password: ")

while True:

    # Current balance
    print(f"\nYour current balance is: {balance}")
    if balance == 0:
        print("*Your balance is low Pleace top up!*")

    # Get user actions
    user_actions = input(
        " \n1.Change Password (P) \n2.Top Up (T) \n3.Reload (R) \n4.Exit (E)\nYour Choice: ").upper()

    # ==============================================
    # Exit
    if user_actions == 'E':
        break

    # Set password
    if user_actions == 'P':
        user_password = input(
            "\nChange password \nEnter your new password: ").upper()

    # Top up
    if user_actions == "T":
        topup_balance = int(input("\nEnter amount to top up: "))
        balance += topup_balance
        continue

    # Reload
    if user_actions == 'R':
        phone_number = int(input("\nEnter the phone number: "))
        reload_amount = int(input("Enter the reload amount: "))
        input_password = input("Enter the password: ")

        if user_password == None:
            print("\nPlz set the password first and try again!")
            continue
        elif user_password != input_password:
            print("\nInvalid password!")
        else:
            # Check the balance < reload amount
            if balance < reload_amount:
                print("INSUFFICIENT BALANCE")
                continue

            balance -= reload_amount
            print("Reload Successful!")

print("\nExit the programme")

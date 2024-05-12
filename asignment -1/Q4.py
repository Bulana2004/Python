while True:

    bill = 0
    # Get the electricity consumption in units
    units = int(input("\nEnter the electricity consumption units: "))

    if units > 50:
        bill += 50 * 5.00

        if units > 150:
            bill += 100 * 7.50

            if units > 250:
                bill += 100 * 12.00

                bill += (units - 250) * 15.00
            else:
                bill = (units - 150) * 12.00

        else:
            bill = (units - 50) * 7.50

    else:
        bill = units * 5.00

    print("\nYour bill total is : Rs:", bill)

    # Get user Choice
    user_choice = input(
        "\nWould you like to do another calculation (yes or no): ")
    x = user_choice[0].lower()
    if x != "y":
        break

while True:
    # Cofee Menu
    coffee_items = {
        "americano_price": 400,
        "latte_price": 350,
        "mocha_price": 690,
        "cappuccino_price": 1225
    }

    print("\nWelcome Star Bucks Coffee Shop \nNo. 142, Dalugama Kelaniya")
    print("\nCofee List and Prices:")

    # print the cofee list
    for item, price in coffee_items.items():
        print(f"{item}: Rs:{price}")

    # Get quantity
    americano_quantity = int(input("\nEnter the quantity of Caffe Americano: "))
    latte_quantity = int(input("Enter the quantity of Caffe Latte: "))
    mocha_quantity = int(input("Enter the quantity of Caffe Mocha: "))
    cappuccino_quantity = int(input("Enter the quantity of Cappuccino: "))

    # Get oder amount
    americano_amount = coffee_items["americano_price"] * americano_quantity
    latte_amount = coffee_items["latte_price"] * latte_quantity
    mocha_amount = coffee_items["mocha_price"] * mocha_quantity
    cappuccino_amount = coffee_items["cappuccino_price"] * cappuccino_quantity

    # Get the total amount
    total_amount = americano_amount + latte_amount + mocha_amount + cappuccino_amount

    # Print the bill
    print("\nStar Bucks Coffee Shop")
    print("No. 142, Dalugama Kelaniya")

    if americano_quantity > 0:
        print(f"\nCaffe Americano\t\t\t\t{
            americano_quantity} * {coffee_items["americano_price"]}\t\tRs:{americano_amount}")
    if latte_quantity > 0:
        print(f"Caffe Latte\t\t\t\t{
            latte_quantity} * {coffee_items["latte_price"]}\t\tRs:{latte_amount}")
    if mocha_quantity > 0:
        print(f"Caffe Mocha\t\t\t\t{
            mocha_quantity} * {coffee_items["mocha_price"]}\t\tRs:{mocha_amount}")
    if cappuccino_quantity > 0:
        print(f"Cappuccino\t\t\t\t{
            cappuccino_quantity} * {coffee_items["cappuccino_price"]}\tRs:{cappuccino_amount}")

    print(f"\nTotal\t\t\t\t\t\t\tRs:{total_amount}")

    user_choice = input("\nDo you want to get another bill (yes or no): ")
    y = user_choice[0].lower()
    if y != "y":
        break

print("\nThank you!")

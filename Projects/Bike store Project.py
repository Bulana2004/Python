bikes = []
item_number = 1
print('\nMadhumala Motor Enterprise')
print('No:356/A, Hill Street, Galle.')
print('011-2345678')

# While loop
while True:
    print("\nMenu")
    print('------')
    # Menu inputs
    user_input = int(input(
        "1.Add new item \n2.Find the bike details and update details \n3.Print the Bill \n4.Exit\nEnter number to continue : ")
    )

    # Add new item to list
    if user_input == 1:
        # Inputs
        print("\nInput Menu")
        print('------------')
        print(f"Item number is {item_number}")
        brand = input("1.Enter brand name : ")
        model = input("2.Enter model name : ")
        quantity = int(input("3.Enter the quantity : "))
        price = float(input("4.Enter the price : Rs."))

        bike_details = {
            "Item number": item_number,
            "Brand": brand,
            "Model": model,
            "Quantity": quantity,
            "Price": price
        }
        # Input dictinoary details to list
        bikes.append(bike_details)
        print("\nItem added successful!")
        # Change the item number
        item_number += 1
        # print(bikes)

    elif user_input == 2:
        print("\nItem List")
        print('-----------')
        for bike_details in bikes:
            print(f"\nItem Number : {bike_details['Item number']} || Brand : {
                  bike_details['Brand']} || Model : {bike_details['Model']}")
        # Get the find number
        enter_item_number = int(
            input("\nEnter item number to find details : "))
        found_item = None

        for bike in bikes:
            if bike["Item number"] == enter_item_number:
                found_item = bike
                break

        if found_item:
            print("\nItem find successful!")
            print('-----------------------')
            print(f"\nItem Number is :{found_item['Item number']} \nBrand is :{
                  found_item['Brand']} \nModal is :{found_item['Model']} \nThe Quantity of bikes :{found_item['Quantity']} \nThe Price of each one bike :Rs.{found_item['Price']}")
            # Update the found item
            choice_update = input(
                "\nDo yo want to update this details\n1.YES\n2.NO\nEnter the number : ")
            if choice_update.lower() == "1":
                new_brand = input(
                    "Enter new Brand (leave blank to keep current details): ")
                new_model = input(
                    "Enter new Model (leave blank to keep current details): ")
                new_quantity = input(
                    "Enter new Quantity (leave blank to keep current details): ")
                new_price = input(
                    "Enter new Price (leave blank to keep current details): ")

                if new_brand:
                    found_item['Brand'] = new_brand
                if new_model:
                    found_item['Model'] = new_model
                if new_quantity:
                    found_item['Quantity'] += int(new_quantity)
                if new_price:
                    found_item['Price'] = float(new_price)

                print("\nItem updated successfully!")
                print('-----------------------------')
                print(f"\nItem Number: {found_item['Item number']} \nBrand: {found_item['Brand']} \nModel: {
                    found_item['Model']} \nQuantity: {found_item['Quantity']} \nPrice: Rs.{found_item['Price']}")
            else:
                print("No updates were made.")
        else:
            print("Item not found.")

    elif user_input == 3:
        print("\nBike list : ")
        print('--------------')
        for bike_details in bikes:
            print(f"Item number {bike_details['Item number']} | Brand {
                  bike_details['Brand']} | Model {bike_details['Model']}")

        choce_input_number = int(
            input("\nEnter item number to make a bill : "))
        found_input_number = None

        for bike in bikes:
            if bike['Item number'] == choce_input_number:
                found_input_number = bike
                break

        # Print the quantity
        if found_input_number:
            print(f"\nCurrent quantity of {found_input_number['Brand']} {
                  found_input_number['Model']} : {found_input_number['Quantity']}")

            buy_quantity = int(input("How many bikes buy the coustermer : "))
            # Test the valid quantity
            if buy_quantity <= found_input_number['Quantity']:
                bill_price = buy_quantity * found_input_number['Price']
                current_quantity = found_input_number['Quantity'] - \
                    buy_quantity

                # Bill Output
                print('\nMadhumala Motor Enterprise')
                print('No:356/A, Hill Street, Galle.')
                print('011-2345678')
                print('----------------------------------------------------------')
                print('Brand\t\tModel\t\tPrice\t\tQuantity')
                print('----------------------------------------------------------')
                print(f"{found_input_number['Brand']}\t\t{
                      found_input_number['Model']}\t\t{found_input_number['Price']}\t\t{buy_quantity}")
                print('-----------------------------------------------------------')
                print(f"Total amount : {bill_price}")

                if current_quantity:
                    found_input_number['Quantity'] = int(current_quantity)
            else:
                print("Invalid Quantity! Enter valid quantity")

    elif user_input == 4:
        break
    else:
        print("Invalid input! Plz try again")

print("\n\tByee!")

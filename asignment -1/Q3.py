coffe_items = []
while True:
    coffe_items = {
        "Caffe Americano": 400.00,
        "Caffe Latte": 359.00,
        "Caffe Mocha": 690.00,
        "Cappuccino": 1225.00
    }

    store_name = "\nStar Bucks Coffee Shop!"
    address = "No,142,Dalugama Kelaniya"

    # Caffe items names
    print(store_name)
    print(address)
    print("\nCoffe Items:")
    for value, key in coffe_items.items():
        print(f"\t{value}- Rs:{key}")

    # quantity
    americano_quantity = int(input("\nAmericano quantity : "))
    latte_quantity = int(input("Latte quantity : "))
    mocha_quantity = int(input("Mocha quantity : "))
    cappuccino_quantity = int(input("Cappuccino quantity : "))

    # Buy Caffe items price
    americano_price = americano_quantity * coffe_items["Caffe Americano"]
    latte_price = latte_quantity * coffe_items["Caffe Latte"]
    mocha_price = mocha_quantity * coffe_items["Caffe Mocha"]
    cappuccino_price = cappuccino_quantity * coffe_items["Cappuccino"]

    # Total price
    total_price = americano_price + latte_price + mocha_price + cappuccino_price

    # Output
    print(store_name)
    print(address)

    if americano_quantity > 0:
        print("\nCaffe Americano\t\t", americano_quantity, "x",
              coffe_items["Caffe Americano"], "\tRs:", americano_price)
    if latte_quantity > 0:
        print("Caffe Latte\t\t", latte_quantity, "x",
              coffe_items["Caffe Latte"], "\tRs:", latte_price)
    if mocha_quantity > 0:
        print("Caffe Mocha\t\t", mocha_quantity, "x",
              coffe_items["Caffe Mocha"], "\tRs:", mocha_price)
    if cappuccino_quantity > 0:
        print("Cappuccino\t\t", cappuccino_quantity, "x",
              coffe_items["Cappuccino"], "\tRs:", cappuccino_price)

    print("\nTotal\t\t\t\t", "       Rs:", total_price)

    # User choice
    choice = input("\nDo you want to got a another bill (yes or no) : ")
    x = choice[0].lower()
    if x != 'y':
        break
print("\nThank you!")

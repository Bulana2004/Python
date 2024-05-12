price = float(input("Enter the price - "))
quantity = float(input("Enter the quantity - "))

amount = price * quantity

if amount >= 1000:
    print("Discount = 10%")
    discount = amount - (amount * 10 / 100)
else:
    print("Discount = 5%")
    discount = amount - (amount * 5 / 100)

print("Your discount is = ", discount)

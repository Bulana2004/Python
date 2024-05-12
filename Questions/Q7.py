# Find the max number
x = int(input("Enter numb1 - "))
y = int(input("Enter numb2 - "))
z = int(input("Enter numb2 - "))

if x > y:
    if x > z:
        max = x
    else:
        max = z

elif y > z:
    max = y

else:
    max = z

print("\nThe max number is = ", max)

# Find min number
x = int(input("\nEnter numb1 - "))
y = int(input("Enter numb2 - "))
z = int(input("Enter numb2 - "))

if x < y:
    if x < z:
        min = x
    else:
        min = z

elif y < z:
    min = y
else:
    min = z

print("\nThe min number is = ", min)

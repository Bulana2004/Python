admition_number = int(input("Enter the admision number - "))

x = admition_number % 4

if x == 0:
    print("Gamunu")
elif x == 1:
    print("Vijaya")
elif x == 2:
    print("Parakum")
else:
    print("Agbo")

# Write a python function to output the multiplication table of given number

def multiplication_numb():
    for i in range(1, 13):
        multiplication = i*numb
        print(numb, "X", i, "=", multiplication)


numb = int(input("Enter the number for Multiplication: "))
multiplication_numb()

def facroruial(no):
    fact = 1
    while no > 0:
        fact = fact * no
        no = no - 1
    print(fact)

# Calling Function
x = int(input("Enter a number: "))
facroruial(x)

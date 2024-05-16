number = int(input("Enter your number to reverse it: "))

reverse_number = 0

while number != 0:
    digit = number % 10
    reverse_number = reverse_number * 10 + digit
    number //= 10

print("Reverce number is: ", str(reverse_number))

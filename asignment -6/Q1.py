max_number = None

# Loop to get 100 inputs from the user
for i in range(1, 101):
    numb = int(input(f"Enter number {i}: "))

    # If user input minus number exit the loop
    if numb < 0:
        break

    # Update max number
    if max_number is None or numb > max_number:
        max_number = numb

print("The maximum number is:", max_number)

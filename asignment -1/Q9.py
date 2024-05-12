original = input("Enter a string: ")

reverse = ""

for i in range(len(original)-1, -1, -1):
    reverse += original[i]

print("Reverse string is: ", reverse)

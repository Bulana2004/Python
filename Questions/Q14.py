# Write a python code to find the maximum number among 10 positive numbers

max = 0

for count in range(1, 11):
    no = int(input("Enter your number = "))

    if no > count:
        max = no
    else:
        max = max
print(max)

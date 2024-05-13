# write a get min number input three numbers
def min(numb1, numb2, num3):
    min_numb = numb1
    if numb2 < min_numb:
        min_numb = numb2
    if numb3 < min_numb:
        min_numb = numb3
    return min_numb


numb1 = int(input("Enter number 1: "))
numb2 = int(input("Enter number 2: "))
numb3 = int(input("Enter number 3: "))

minimum = min(numb1, numb2, numb3)
print("The minimum number is: ", minimum)

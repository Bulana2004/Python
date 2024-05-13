# Write a python function to find the maximum number of three input intigers

def find_maxnumb(numb1, numb2, numb3):
    max_numb = numb1
    if numb2 > max_numb:
        max_numb = numb2
    if numb3 > max_numb:
        max_numb = numb3
    return max_numb


numb1 = int(input("Enter number 1: "))
numb2 = int(input("Enter number 2: "))
numb3 = int(input("Enter number 3: "))

maximum = find_maxnumb(numb1, numb2, numb3)
print("Maximum number is ", maximum)

# Input marks and get avarage and grade

p = float(input("Enter your Physics marks: "))
c = float(input("Enter your Chemestry marks: "))
b = float(input("Enter your Biology marks: "))
maths = float(input("Enter your Mathematics marks: "))
com = float(input("Enter your Computer marks: "))

# Get total marks
total = p+c+b+maths+com
print("\nYour total marks are ", total)

# Get avarage
avarage = total/5
print("Your avarage marks are ", avarage)

# Get grade pass
x = avarage
if x <= 40:
    grade = "F"
elif x <= 60:
    grade = "E"
elif x <= 70:
    grade = "D"
elif x <= 80:
    grade = "C"
elif x <= 90:
    grade = "B"
elif x <= 100:
    grade = "A"
else:
    grade = "Invalid Marks"
print("You got:", grade)

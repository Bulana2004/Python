M1 = int(input("Enter the marks - "))
M2 = int(input("Enter the marks - "))

total = M1 + M2
avg = total / 2

if avg >= 75:
    print("\nA")
elif avg >= 65:
    print("\nB")
elif avg >= 55:
    print("\nC")
elif avg >= 35:
    print("\nS")
else:
    print("\nF")

max = 0
i = 0

for i in range (1,101):
    x=int(input("Enter : "))

    if x < 0:
        break
    
    if max == 0 or x > max:
        max = x

print(f"max is {max}")

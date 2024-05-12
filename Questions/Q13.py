# Write a python code to find the total of odd numbers and the total of even numbers separately 1 to 10

totaleven = 0
totalodd = 0

for count in range(1, 11):
    r = count % 2

    if r == 0:
        totaleven = totaleven + count
    else:
        totalodd = totalodd + count

print(totaleven, totalodd)

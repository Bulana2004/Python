l = [8, 5, 4, 2, 1]

for k in range (0, len(l)-1):
    for j in range(0, len(l)-1):
        if l[j] > l[j+1]:   
            l[j], l[j+1] = l[j+1], l[j]

print(l)

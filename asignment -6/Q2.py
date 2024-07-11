L = [23, 45, 32, 11, 67, 39, 92, 51, 74, 89]
K = 38

n = len(L)
i = 0

while i < n:
    if L[i] == K:
        print("Output TRUE")
    else:
        i += 1

print("Output FALSE")

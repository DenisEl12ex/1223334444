k = int(input())
kol = 0
for i in range(k):
    for j in range(i):
        if kol == k:
            break
        else:
            print(i, end=" ")
kol += 1
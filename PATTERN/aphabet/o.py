n = int(input())
for i in range(n):
    for j in range(n-2):
        if (j == 0 and (i >= 1 and i < n-1)) or (i == 0 and (j >= 1 and j < n-2-1 )) or (j == n-2-1 and (i >= 1 and i < n-1)) or (i == n-1 and (j >= 1 and j < n-2-1 )):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


n = int(input())
k = n*2 + 3
for i in range(n):
    for j in range(k):
        if (j == 0 and (i >= 0 and i < n)) or (j == k-1 and (i >= 0 and i < n)):
            print("*",end="")
        elif (i == 0 and (j >= 0 and j < k )) or (i == n-1 and (j >= 0 and j < k )):
            print("*",end="")
        else:
            print(" ",end="")
    print()
k
n=7
for i in range(n):
    for j in range(n-2):
        if i == 0 or i == n-1 or (i == n // 2) or j == 0:
            print("*",end="")
        else:
            print(" ",end="")
n = 7
for i in range(n):
    for j in range(n-2):
        if j == 0 or i == n-1:
            print("*",end="")
        else:
            print(" ",end="")
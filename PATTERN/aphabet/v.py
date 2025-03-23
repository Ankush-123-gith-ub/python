n=7
for i in range(n):
    for j in range(n*2):
        if i == j or j == n*2 - i - 2:
            print("*",end="")
        else:
            print(" ",end="")
n = 6

for i in range(n):
    for j in range(n * 2):
        if i == j or j == (n * 2 - i - 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()


for j in range(n*2):
        if i == j or (j == n + i and i == n - i - 1):
            print("*",end="")
        else:
            print(" ",end="")    
 
n = int(input("Enter: "))
for i in range(n):
    for j in range(n-2):
        if i == 0 or i == n-1 or (n-2) // 2 == j:
            print("*",end="")
        else:
            print(" ",end="")

n = int(input("enter the row: "))
for i in range(n,0,-1):
    for j in range(0,n-i):
        print(end=" ")
    for j in range(i-1):
        print("*",end="")
    for j in range(i):
        print("*",end="")
    print()
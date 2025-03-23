n = int(input("enter the row and column: "))
for i in range(0,n):
    for j in range(n-i,1,-1):
        print(end=" ")
    for j in range(i):
        print("*",end="")
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(end=" ")
    for j in range(i):
        print("*",end="")
    for j in range(i-1):
        print("*",end="")
    print()


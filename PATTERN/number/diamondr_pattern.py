n = int(input())
for i in range(n):
    for j in range(i+1,n):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    for j in range(i):
        print("*",end="")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i+1,n):
        print("*",end="")
    for j in range(i+2,n):
        print("*",end="")
    print()

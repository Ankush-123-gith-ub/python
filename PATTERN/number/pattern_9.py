n = int(input("Enter the number: "))
for i in range(n):
    for j in range(i+1,n):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()
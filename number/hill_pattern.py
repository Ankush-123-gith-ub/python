n=int(input("enter the row = "))
for i in range(n):
    for j in range(n-i,0,-1):
        print(end=" ")
    for j in range(i):
        print("*",end="")
    for j in range(i+1):
        print("*",end="")


    print()
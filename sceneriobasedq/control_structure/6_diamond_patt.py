n= int(input("Enter the rows: "))
for i in range(0,n,2):
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(n-2,0,-2):
    for j in range(i):
        print("*",end="")
    print()
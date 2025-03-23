n = int(input("Enter: "))
for i in range(n):
    for j in range(i,n-1):
        print(" ",end="")
    for j in range(i+1+i):
        print(j+1,end="")
    print()
for i in range(n-1):
    for j in range(i+1):
        print(" ",end="")
    for j in range(1, 2*i+2):
        print(j, end=" ")
    print()
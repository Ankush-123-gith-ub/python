n = int(input("Enter: "))
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range(1,n+1-i):
        print(j,end="")
    print()
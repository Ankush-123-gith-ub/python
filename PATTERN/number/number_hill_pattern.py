n = int(input("Enter: "))
for i in range(n):
    for j in range(i,n-1):
        print(" ",end="")
    for j in range(i+1+i):
        print(j+1,end="")
    print()
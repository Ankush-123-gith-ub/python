n = int(input("Enter: "))
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(j+1,end=" ")
    print()
for i in range(n-1):
    for j in range(1,n-i):
        print(j,end=" ")
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(1,n-i):
        print(j,end=" ")
    print()


    
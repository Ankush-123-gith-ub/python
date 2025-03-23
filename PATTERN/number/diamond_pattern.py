n = int(input())
p = 1
for i in range(n):
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(p,end=" ")
    for j in range(i):
        print(p,end=" ")
    p = p + 1
    print()
n = n - 1
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(p,end=" ")
    for j in range(i,n-1):
        print(p,end=" ")
    p = p + 1
    print()

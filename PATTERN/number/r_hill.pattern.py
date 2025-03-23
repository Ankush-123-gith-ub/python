n = int(input())
p = 5
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        print(p,end=" ")
    for j in range(i,n-1):
        print(p,end=" ")
    p = p - 1
    print()
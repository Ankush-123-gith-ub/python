n = int(input())
for i in range(n):
    for j in range(i,n-1):
        print(" ",end="")
    for j in range(i+1):
        print(i+1,end="")
    for j in range(i):
        print(i+1,end="")
    print()
p  = n -1
for i in range(n-1):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n-1):
        print(p,end="")
    for j in range(i,n-2):
        print(p,end="")
    p = p - 1
    print()
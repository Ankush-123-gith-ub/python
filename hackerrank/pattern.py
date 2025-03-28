n = int(input())
for i in range(n):
    for j in range(i,n-1):
        print(" ",end="")
    for j in range(i*2+1):
        print("H",end="")
    print()
for i in range(n+1):
    for j in range(n*8+1):
        if (j >= n-3 and j <= n+1) or (j >= n*4+2 and j <= n*5+1):
            print("H",end="")
        else:
            print(" ",end="")
    print()
for i in range(n-2):
    for j in range(n*6+1):
        if (j >= n-3 and j <= n*5+1):
            print("H",end="")
        else:
            print(" ",end="")
    print()
for i in range(n+1):
    for j in range(n*8+1):
        if (j >= n-3 and j <= n+1) or (j >= n*4+2 and j <= n*5+1):
            print("H",end="")
        else:
            print(" ",end="")
    print()
for i in range(n):
    for j in range(n*6+1):
        if j >= n*4+i and j <= (n*5+3) - i:
               print("H",end="")
        else:
            print(" ",end="")
    print()

    
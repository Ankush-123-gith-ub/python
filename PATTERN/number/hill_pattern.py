n= int(input())
p = 5
for i in range(n):
    for j in range(i,n-1):
        print(" ",end="")
    for j in range(i+1):
        if i % 2 == 0:
            print("a",end="")  # change with *
        elif i % 2 != 0:
            print("b",end="")
    for j in range(i):
        if i % 2 == 0:
            print("a",end="")  # change with *
        elif i % 2 != 0:
            print("b",end="")
    p = p - 1
    print()
    
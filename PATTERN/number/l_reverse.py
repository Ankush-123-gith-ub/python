n = int(input())
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range(i,n):
        if i % 2 == 0:
            print("#",end="")  # change with *
        elif i % 2 != 0:
            print("$",end="")
    print()
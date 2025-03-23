size = int(input())
for i in range(size):
        for j in range(i,size-1):
            print(" ",end="")
        p = 96 + size
        for j in range(i+1):
            print(chr(p),end="")
            p -= 1
        p = p + 2
        for j in range(i):
            print(chr(p),end="")
            p += 1
        for j in range(i,size-1):
            print(" ",end="")
        print()
for i in range(size-1):
        for j in range(i+1):
            print(" ",end="")
        p = 96 + size
        for j in range(i,size-1):
            print(chr(p),end="")
            p -= 1
        p = p + 2
        for j in range(i,size-2):
            print(chr(p),end="")
            p += 1
        for j in range(i+1):
            print(" ",end="")
        print()
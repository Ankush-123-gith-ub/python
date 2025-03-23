n = int(input())
k = 65
for i in range(n):
    p = k
    for j in range(i+1):
        print(chr(p),end=" ")
        p += 1
        k += 1
    print()

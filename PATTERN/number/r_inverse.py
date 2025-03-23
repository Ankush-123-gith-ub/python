n = int(input())
p = 0
for i in range(n):
    
    for j in range(i+1):
        print(p,end="")  # change with *
    p = p + 2
    print()

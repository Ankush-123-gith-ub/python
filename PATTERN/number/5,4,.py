n = int(input("Enter: "))
for i in range(n):
    p = 5
    for j in range(i+1):
        print(p,end="")
        p = p - 1
    print() 
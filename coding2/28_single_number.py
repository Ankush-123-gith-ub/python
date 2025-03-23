n = list(map(int,input("Enter the numbers: ").split()))
for i in n:
    if n.count(i) == 1:
        print(i)

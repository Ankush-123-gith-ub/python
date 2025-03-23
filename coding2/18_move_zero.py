n = list(map(int,input("Enter the numbers: ").split()))
for i in range(len(n)-1):
    for i in range(len(n)-1):
            if n[i] == 0:
                temp = n[i]
                n[i] = n[i+1]
                n[i+1] = temp
print(n)
            



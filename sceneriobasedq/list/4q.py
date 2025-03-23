n = list(map(int,input("Enter the numbers: ").split()))
t = int(input("Target: "))
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i] + n[j] == t:
            print([i,j])
            exit()
            


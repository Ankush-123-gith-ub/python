n = int(input("Enter the number: "))
for i in range(2,n+1):
    for j in range(2,10):
        if i % j == 0:
            print(i)
            break
            


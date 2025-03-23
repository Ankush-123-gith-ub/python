n = int(input("Enter: "))
for i in range(n):
    for j in range(n-2):
        if i == 0 or i == n-1 or (n-2) // 2 == j:
            print("*",end="")
        else:
            print(" ",end="")

    for j in range(2):
        print(" ",end=" ")

    for j in range(n-2):
        if j == 0 or i == n-1:
            print("*",end="")
        else:
            print(" ",end="")

    for j in range(1):
        print(" ",end="")
    
    for j in range(n-2):
        if (j == 0 and (i >= 1 and i < n-1)) or (i == 0 and (j >= 1 and j < n-2-1 )) or (j == n-2-1 and (i >= 1 and i < n-1)) or (i == n-1 and (j >= 1 and j < n-2-1 )):
            print("*",end="")
        else:
            print(" ",end="")
    
    for j in range(1):
        print(" ",end="")

    for j in range(n*2):
        if i == j or j == n*2 - i - 2:
            print("*",end="")
        else:
            print(" ",end="")  

    for j in range(n-2):
        if i == 0 or i == n-1 or (i == n // 2) or j == 0:
            print("*",end="")
        else:
            print(" ",end="")  
    print()
 

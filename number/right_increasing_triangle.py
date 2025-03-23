n=int(input("enter the row= "))
# for rows
for i in range(1,n+1):
    #for columns
    for j in range(1,i+1):
        print("*",end="")
    print()
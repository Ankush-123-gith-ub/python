n = tuple(map(str,input("Enter the strings: ").split()))
temp = []
for i in n:
    if i not in temp:
        temp.append(i)      
print(tuple(temp))


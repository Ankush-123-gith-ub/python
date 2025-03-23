t = int(input("Enter the testcase: "))
temp = []
for i in range(t):
    n = int(input("Enter the number: "))
    temp.append(n)
print(temp)
for i in range(len(temp)):
    for j in range(len(temp) -1):
        if temp[j] == 0:
            a = temp[j]
            temp[j] = temp[j+1]
            temp[j+1] = a
print(temp)
    
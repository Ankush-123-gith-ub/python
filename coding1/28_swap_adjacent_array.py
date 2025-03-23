t = int(input("Enter the testcase: "))
temp = []
for i in range(t):
    n = int(input("Enter the number: "))
    temp.append(n)

if len(temp) % 2 == 0:
    p = 0
    for i in range(int((len(temp))/2)):
        a = temp[p]
        temp[p] = temp[p+1]
        temp[p+1] = a
        p = p + 2
else:
    p = 0
    for i in range(int(((len(temp))+1)/2) -1 ):
        a = temp[p]
        temp[p] = temp[p+1]
        temp[p+1] = a
        p = p + 2
print(temp)


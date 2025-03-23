t = int(input("Enter the testcase: "))
temp = []
for i in range(t):
    n = int(input("Enter the number: "))
    temp.append(n)

if len(temp) % 2 == 0:
    for i in range(int((len(temp))/2)):
        a = temp[i]
        temp[i] = temp[(-i)-1]
        temp[(-i)-1] = a
else:
    for i in range(int(((len(temp))+1)/2)):
        a = temp[i]
        temp[i] = temp[(-i)-1]
        temp[(-i)-1] = a
print(temp)


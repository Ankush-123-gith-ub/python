t = int(input("Enter the testcase: "))
temp = []
for i in range(t):
    n = int(input("Enter the number: "))
    temp.append(n)
if sum(temp) % len(temp)== 0:
    print(int(sum(temp) / len(temp)))
else:
    print(-1)
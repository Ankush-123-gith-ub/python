t = int(input("Enter the testcase: "))
temp = []
for i in range(t):
    n = int(input("Enter the number: "))
    temp.append(n)
print(f"The maximum roots: {max(temp)}")
t = int(input("Enter the testcase: "))
temp = []
for i in range(t):
    n = int(input("Enter the number: "))
    temp.append(n)
e = int(input("Enter the number to be deleted: "))
new_temp = []
for i in temp:
    if i != e:
        new_temp.append(str(i))
if e in temp:
    print(" ".join(new_temp))
else:
    print("Not found.")
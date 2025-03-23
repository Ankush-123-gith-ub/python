department_a = tuple(map(int,input("Enter the strings: ").split(",")))
department_b = tuple(map(int,input("Enter the strings: ").split(",")))
n = department_a + department_b
print(n)
temp = []
for i in n:
    if i not in temp:
        temp.append(i)      
print(tuple(temp))
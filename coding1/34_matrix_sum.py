m = int(input("Enter rows: "))
n = int(input("Enter columns: "))
temp = []
for i in range(m*n):
    a = int(input(f"Enter {i+1} number: "))
    temp.append(a)
mul = 1
for i in temp:
    mul *= i
print(f"{sum(temp)} {mul}")

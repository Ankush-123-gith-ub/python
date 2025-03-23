n = list(map(int,input("Enter the numbers: ").split()))
# s = sorted(n)
# print(s)
temp = []
m = max(n)
for i in n:
    if i != m:
        temp.append(i)
print(temp)
if temp == []:
    print("No seccond high score.")
else:
    print(max(temp))





n = tuple(map(int,input("Enter the numbers: ").split(",")))
sum = 0
count = 0
for i in n:
    sum += i
    count += 1
# print(round((sum/count),2))
print(f"{(sum/count):.2f}")
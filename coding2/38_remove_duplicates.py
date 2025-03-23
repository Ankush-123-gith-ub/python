# n = list(map(int,input().split()))
# print(list(set(n)))

n = list(map(int,input().split()))
temp = []
for i in n:
    if i not in temp:
        temp.append(i)
print(temp)
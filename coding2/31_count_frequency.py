n = input()
temp = {}
for i in n:
    if i not in temp:
        temp[i] = n.count(i)
print(temp)
#  temp[i].append(n.count(i))
t = int(input("Enter the no. of sublist: "))
n = []
for i in range(t):
    sub_list = list(map(int,input("Enter the lists number: ").split()))
    n.append(sub_list)
print(n)
len_i = len(n[0])
temp = []
for i in n:
    sum = 0
    for j in i:
        sum += j
    temp.append(sum)
for i in range(len_i):
    sum = 0
    for j in n:
        sum += j[i]
    temp.append(sum)
print(temp)





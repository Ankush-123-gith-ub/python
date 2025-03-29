a = (input()).split()
temp = []
z = eval(a[0])
for i in range(1,len(a)):
    a[i] = eval(a[i])
    for j in a[i]:
        if j in z:
            temp.append(j)
    z = temp
temp3 = []
print(temp)
m = max(temp)
for i in temp:
    if temp.count(i) > 1:
        temp3.append(i)
print(list(set(temp3)))

   


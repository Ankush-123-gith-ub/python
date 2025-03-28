# n_a = list(map(str,input().split()))
# n_b = list(map(str,input().split()))
# a = []
# b = []
# for i in n_a:
#     if i.isdigit():
#         a.append(int(i))
#     else:
#         a.append((i))
# for i in n_b:
#     if i.isdigit():
#         b.append(int(i))
#     else:
#         b.append((i))
# temp = []
# count = 0
# if len(a) <= len(b):
#     for i in range(len(a)):
#         temp.append(a[i])
#         temp.append(b[i])
#     for i in range(len(a),len(b)):
#         temp.append(b[i])
# if len(b) <= len(a):
#     for i in range(len(b)):
#         temp.append(a[i])
#         temp.append(b[i])
#     for i in range(len(b),len(a)):
#         temp.append(a[i])
# print(temp)

n_a = list(map(str,input().split()))
n_b = list(map(str,input().split()))
a = []
b = []
for i in n_a:
    if i.isdigit():
        a.append(int(i))
    else:
        a.append((i))
for i in n_b:
    if i.isdigit():
        b.append(int(i))
    else:
        b.append((i))
temp = []
count = 0
if len(a) <= len(b):
    temp2 = (list(zip(a,b[:(len(a))])))
    for i in temp2:
        for j in i:
            temp.append(j)
    for i in range(len(a),len(b)):
        temp.append(b[i])
if len(b) <= len(a):
    temp2 = (list(zip(a,b[:(len(b))])))
    for i in temp2:
        for j in i:
            temp.append(j)
    for i in range(len(b),len(a)):
        temp.append(a[i])
print(temp)

 
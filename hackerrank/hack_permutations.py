from itertools import permutations
a,b = map(str,input().split())
b  = int(b)
c = sorted(list(permutations(a,b)))
for i in c:
    print("".join(i))
# temp = set()
# for i in a:
#     for j in a:
#             z = i+j
#             temp.add(z)
# temp = sorted(temp)
# for i in temp:
#     print(i)
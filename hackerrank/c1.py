n = input()
m = n.split()
a = m[0]
b = eval(m[1])
for i in b:
    if sorted(a) == sorted(i):
        print(i)



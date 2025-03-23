a = {"a": 10, "b": 20, "c": 5}
b = {"x": 100, "y": 200, "z": 50}
c = {"apple": 3, "banana": 7}
d = {"p": 1, "q": 5, "r": 10}
e = {"math": 75, "science": 80}

t = int(input("Enter the target value: "))
key_d = []
for key,value in c.items():
    if value < t:
        key_d.append(key)
for i in key_d:
    del c[i]
print(c)

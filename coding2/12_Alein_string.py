n = input()
length = len(n)
new_s = []
for i in range(length):
    if n[i].isspace():
        new_s.append(n[i])
    else:
        new_s.append(chr((ord(n[i]))+1))
print("".join(new_s))

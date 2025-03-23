s = input()
length = len(s)
new_s = []
print(length)
for i in range(length):
    if i % 2 == 0:
        new_s.append(chr(ord(s[i]) - 2))
    if i % 2!= 0:
        new_s.append(chr(ord(s[i]) + 2))
print("".join(new_s))

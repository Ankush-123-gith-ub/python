n = input()
length = len(n)
new_s = []
for i in range(length):
    if i % 2 == 0:
        new_s.append((n[i]).upper())
    if i % 2 != 0:
        new_s.append((n[i]).lower())
print("".join(new_s))


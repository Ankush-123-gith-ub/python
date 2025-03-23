# string (each word reverse at its place)
s = input()
a = s.split()
b = ""
for i in a:
    b = b + i[::-1] + " "
print(b)


# list (each word reverse at its place )
s = input()
a = s.split()
b = []
for i in a:
    b.append(i[::-1])
print(" ".join(b))


# list (reverse)
s = input().split()
b = s[::-1]
print(" ".join(b))


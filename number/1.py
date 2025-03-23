a = input("")
b = a.split()
for i in b:
    if int(i) <= 26:
        c = chr(int(i)+64)
        print(c,end="")
    elif int(i) > 26:
        c = chr(int(i)+70)
        print(c,end="")
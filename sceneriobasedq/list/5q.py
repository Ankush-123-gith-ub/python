n = input("Enter the string: ").split()
s = input("Enter the string to be checked: ")
count = 0
temp = ""
for i in n:
    if len(i) >= len(s) and i[0] == s[0]:
        for j in range(len(s)):
            temp += i[j]
        temp += " "
    
for i in temp.split():
    if s in i:
        count += 1
print(count)



n = input().replace(" ","")
temp = ""
for i in n:
    if i not in temp:
        temp += i
    else:
        temp += i.replace(i,"-")
print(temp)
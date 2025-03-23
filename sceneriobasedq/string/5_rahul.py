n = input("Enter the string: ")
temp = []
long_temp = []
for i in range(len(n)):
    temp_string = ""
    for j in range(i,len(n)):
        temp_string += n[j]
        if temp_string == temp_string[::-1]:
            temp.append(temp_string)
len_i = []
for i in temp:
    len_i.append(len(i))
for i in temp:
    if len(i) == max(len_i):
        long_temp.append(i)
print(long_temp[0])




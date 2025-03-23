n = input("Enter the string: ")
k = int(input("Enter the max length: "))
dict_c = {}
max_len = []
length = 0
for i in range(len(n)):
    sum = 0
    char = n[i]
    if char in dict_c:
        dict_c[char] += 1
    else:
        dict_c[char] = 1
    
    if len(dict_c) == k:
        for j in dict_c.values():
            sum += j
            max_len.append(sum)
        
    while(len(dict_c) > k ):
        dict_c[n[length]] -=1
        if dict_c[n[length]] == 0:
            del dict_c[n[length]]
        length += 1

        if len(dict_c) == k:
            for j in dict_c.values():
                sum += j
                max_len.append(sum)
print(max(max_len))
            
    
        



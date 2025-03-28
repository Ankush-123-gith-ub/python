n = eval(input())
rev_n = n[::-1]
new_list = []
while rev_n:
    item = rev_n.pop()
    if isinstance(item,list):
        rev_n.extend(item[::-1])
    else:
        new_list.append(item)
print(new_list)


    
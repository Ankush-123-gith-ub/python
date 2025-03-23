def rem(list,word):
    n=[]
    for item in list:
        if not(item==word):
            n.append(item.strip(word))  ## important 
    return n
list=["harry","rohan","harshita"]
word=input("Enter the name: ")
print(rem(list,word))
# input = Ravan 
# output = Rav1n
n = input()
temp = []
a=''
count=0
for i in n:
    if i not in a:
        a+=i
        count+=1
    else:
        a += str(n.index(i))
print(a)


        

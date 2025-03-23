t = int(input("Enter the testcase: "))
temp = []
for i in range(t):
    n = int(input("Enter the number: "))
    temp.append(n)
str = ""
for i in temp:
    if i % 2 == 0:
        str += "0 "
        
    else:
        str += "1 "    
print(str)
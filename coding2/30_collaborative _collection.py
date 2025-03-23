a = input("Enter first string: ")
b = input("Enter second string: ")
temp = []
min_length  = min(len(a),len(b)) 
for i in range(min_length):
            temp.append(a[i]+b[i])    
if len(a) > len(b):
        temp.append(a[min_length:])
if len(a) < len(b):
        temp.append(b[min_length:])
print("".join(temp))

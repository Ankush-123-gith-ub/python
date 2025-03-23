a = int(input("Enter first: "))
b = int(input("Enter second: "))
temp1 = []
for i in range(2,10):
    while a % i == 0:
        a = a // i
        temp1.append(i)
        
temp2 = []  
for i in range(2,10):
    while b % i == 0:
        b = b // i
        temp2.append(i)
hcf = 1
for i in temp1:
    if i in temp2:
        hcf *= i
print(hcf)
       
        
    

            

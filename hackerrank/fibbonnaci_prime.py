n = int(input())
fibbonaci = []
a = 0 
fibbonaci.append(a)
b = 1
fibbonaci.append(b)
for i in range(n+1):
    sum = a+b
    fibbonaci.append(sum)
    a = b
    b = sum
print(fibbonaci)
for i in fibbonaci:
    if i >= 2:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i,end=" ")
            

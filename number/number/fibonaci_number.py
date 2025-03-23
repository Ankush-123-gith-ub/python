n = int(input())
a = 0
print(a,end=" ")
b = 1 
print(b,end=" ")
while n != 0:
    temp = a + b
    print(temp,end=" ")
    a = b 
    b = temp
    n -= 1


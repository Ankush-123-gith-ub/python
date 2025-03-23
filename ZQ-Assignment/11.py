a = int(input())
b = int(input())
if (a>b):
    a = a - b
    b = a + b
    a = b - a
elif (b>a):
    b = b - a
    a = b + a
    b = a - b
print(a,b)
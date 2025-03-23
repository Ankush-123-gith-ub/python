# n  = int(input("Enter the num: "))
# a = n % 10
# b = int(n/10) % 10
# c = int(int(n/10) / 10)
# d = 1
# e = 1
# f = 1
# for i in range(1,a+1):
#     d = d*i
# for i in range(1,b+1):
#     e = e*i
# for i in range(1,c+1):
#     f = f*i
# if (d+e+f) == n:
#     print("This is krishna murti number.")
# else:
#     print("This is not krishna murti number.")
def fact(n):
    a = 1
    for i in range(1,n+1):
        a = a * i
    return a
n  = int(input("Enter the num: "))
temp = n
b = 0
while n>0:
    a = n % 10
    b = fact(a) + b
    n = n // 10
if temp == b:
    print("This is krishna murti number.")
else:
    print("This is not krishna murti number.")





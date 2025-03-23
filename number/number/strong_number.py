def fact(n):
    mul = 1
    for i in range(1,n+1):
        mul *= i
    return mul

n = int(input())
temp = n
sum = 0
while n != 0:
    a = n % 10
    sum += fact(a)
    n = n // 10
print(sum)
if temp == sum:
    print("Strong NUmber.")
else:
    print("Not Strong NUmber.")

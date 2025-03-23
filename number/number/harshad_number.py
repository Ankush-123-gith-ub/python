n = int(input())
temp = n
sum = 0
while n != 0:
    a = n % 10
    sum = sum + a
    n = n // 10
print(temp)
print(sum)
if temp % sum == 0:
    print("Harshad Number.")
else:
    print("Not Harshad Number.")
n = int(input("Enter the number: "))
temp = n
len = len(str(n))
sum = 0
while n > 0:
    a = n % 10
    sum = a**(len) + sum
    n = n // 10
if sum == temp:
    print("This is an armstrong number.")
else:
    print("Not an armstrong number.")
s = int(input())
n = s*s
sum = 0
while n > 0:
    a = n % 10
    sum += a
    n = n // 10
if sum == s:
    print("Neon number.")
else:
    print("Not neon number.")

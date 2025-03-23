n = int(input("Enter the number: "))
while len(str(n)) > 1:
    sum = 0
    while n > 0:
        a = n % 10
        sum += a
        n //= 10
    n = sum
print(sum)
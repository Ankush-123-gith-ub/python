n = int(input("Enter the number: "))
a = n**2
b = 0
while a > 0:
    c = a % 10
    b = c + b
    a = a // 10
if b == n:
    print("This is Neon number.")
else:
    print("This is not a neon number.")

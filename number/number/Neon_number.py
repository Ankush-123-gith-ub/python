n = int(input("Enter: "))
temp = n
square = n * n
sum = 0
while square != 0:
    a = square % 10
    sum = sum + a
    square = square // 10
if temp == sum:
    print("Neon Number.")
    print(sum)
else:
    print("NOt Neon Number.")
    print(sum)


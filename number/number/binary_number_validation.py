n = int(input("Enter: "))
is_binary = True
while n != 0:
    a = n % 10
    if a != 0 and a !=1:
        is_binary = False
        break
    n = n // 10
if is_binary:
    print("Binary Number.")
else:
    print("Not Binary Number.")




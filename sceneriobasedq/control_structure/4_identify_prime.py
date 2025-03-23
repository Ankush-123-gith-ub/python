n = int(input("Enter the number: "))
for i in range(2,n):
    if n % i == 0:
        print("False")
        break
else:
    if n < 2:
        print("False")
    else:
        print("True")

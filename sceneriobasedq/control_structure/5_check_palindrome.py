n = int(input("Enter the number: "))
temp = n
sum =  0
while n > 0:
    r = n % 10
    sum = (10*sum) + r
    n = n // 10
if temp == sum:
    print("Palindrome.")
else:
    print("Not palindrome.")
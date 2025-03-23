n = int(input("Enter the number: "))
temp = n
sum = 0
while n>0:
    a = n % 10
    sum  = (10*sum) + a
    n = n // 10
if sum == temp:
    print("Palindrome.")
else:
    print("Not Palindrome.")

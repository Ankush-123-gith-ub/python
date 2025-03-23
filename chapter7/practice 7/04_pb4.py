n=int(input("Enter the number: "))
if(n < 1):
    print("Given  number is not prime")
for i in range(2,n):
    if((n % i) == 0):
        print("Given  number is not prime")
        break
else:
    print("Given  number is prime")

n = int(input())
is_prime = True
if n < 2 :
    is_prime = False
for i in range(2,n):
    if n % i == 0:
        is_prime = False
if is_prime:
    print("Prime number.")
else:
    print("Not Prime number.")
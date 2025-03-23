# using for loop 
# n1 = int(input("Enter the number1: "))
# n2 = int(input("Enter the number2: "))
# for i in range(n1,n2+1):
#     if i > 1:  # Prime numbers are greater than 1
#         is_prime = 1
#         for j in range(2,i):
#             if i % j == 0:
#                 is_prime = 0
#                 break
#         if is_prime:
#             print(i,end = " ")
  
# using while loop
n1 = int(input("Enter the number1: "))
n2 = int(input("Enter the number2: "))
i = n1
while i < n2:
    if i > 1:
        isprime = 1
        j = 2
        while j < i:
            if i % j == 0:
                isprime = 0
                break
            j = j + 1
        if isprime:
            print(i,end = " ")
    i = i+1
        
    
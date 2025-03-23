import math
n = int(input())
for i in  range(2,n):
     for j in range(2,i):
            if i % j == 0:
                break
     else:
        print(i,end=" ")
# import math
# n = int(input("Enter a number: "))
# for i in range(2, n):
#     is_prime = True  # Assume i is prime
#     for j in range(2, int(math.sqrt(i)) + 1):  
#         if i % j == 0:  # If i is divisible by j, it's not prime
#             is_prime = False
#             break  # Stop checking further
    
#     if is_prime:
#         print(i, end=" ")  # Print only if it's confirmed prime
           
    

            
        


